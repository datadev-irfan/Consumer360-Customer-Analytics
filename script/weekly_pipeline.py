# =========================
# WEEKLY ANALYTICS PIPELINE
# =========================

import pandas as pd
from sqlalchemy import create_engine
from mlxtend.frequent_patterns import apriori, association_rules
from datetime import datetime
import logging
import os

# -----------------------------------------
# 0. LOGGING SETUP
# -----------------------------------------
LOG_DIR = "D:/consumer360_project/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/weekly_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("===== Weekly Pipeline Started =====")

try:

    # -------------------------
    # 1. DATABASE CONNECTION
    # -------------------------
    logging.info("Connecting to MySQL database")
    engine = create_engine(
        "mysql+pymysql://root:root@localhost/consumer360_dw"
    )
    logging.info("Database connection successful")

    # -------------------------
    # 2. LOAD SALES + REGION
    # -------------------------
    logging.info("Loading sales data")
    query = """
    SELECT
        c.customer_id,
        c.region,
        f.order_id,
        t.date_time AS order_date,
        f.total_price
    FROM consumer360_dw.fact_sales f
    JOIN consumer360_dw.dim_customer_region c
        ON f.customer_key = c.customer_key
    JOIN consumer360_dw.dim_time t
        ON f.time_key = t.time_key;"""
    sales_df = pd.read_sql(query, engine)
    logging.info(f"Loaded {len(sales_df)} sales records")

    # -----------------------------------------
    # 3. CUSTOMER LATEST REGION
    # -----------------------------------------
    logging.info("Deriving latest customer region")

    sales_df = sales_df.sort_values("order_date")

    customer_region = (
        sales_df
        .groupby("customer_id")
        .tail(1)[["customer_id", "region"]]
    )

    # -------------------------
    # 4. RFM ANALYSIS
    # -------------------------
    logging.info("Starting RFM analysis")
    reference_date = sales_df['order_date'].max() + pd.Timedelta(days=1)

    rfm = sales_df.groupby('customer_id').agg({
        'order_date': lambda x: (reference_date - x.max()).days,
        'order_id': 'count',
        'total_price': 'sum'
    }).reset_index()
    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']


    # RFM SCORING
    rfm['R_score'] = pd.qcut(rfm['recency'], 5, labels=[5,4,3,2,1])
    rfm['F_score'] = pd.qcut(rfm['frequency'], 5, labels=[1,2,3,4,5])
    rfm['M_score'] = pd.qcut(rfm['monetary'], 5, labels=[1,2,3,4,5])

    rfm['RFM_Score'] = (
        rfm['R_score'].astype(str) +
        rfm['F_score'].astype(str) +
        rfm['M_score'].astype(str)
    )

    # SEGMENTATION
    def segment_customer(row):
        if row['R_score'] >= 4 and row['F_score'] >= 4 and row['M_score'] >= 4:
            return 'Champion'
        elif row['R_score'] >= 3 and row['F_score'] >= 3:
            return 'Loyal'
        elif row['R_score'] >= 2:
            return 'Hibernating'
        else:
            return 'Potential'

    rfm['segment'] = rfm.apply(segment_customer, axis=1)
    # Add Region
    rfm = rfm.merge(customer_region, on="customer_id", how="left")

    rfm.to_sql(
        "rfm_customer_scores",
        engine,
        if_exists="replace",
        index=False
    )

    logging.info("RFM analysis completed successfully")
    # -------------------------
    # 5. MARKET BASKET ANALYSIS
    # -------------------------
    logging.info("Starting Market Basket Analysis")
    query_mba = """
    SELECT
        c.customer_id,
        i.item_name
    FROM consumer360_dw.fact_sales f
    JOIN consumer360_dw.dim_item i
        ON f.item_key = i.item_key
    JOIN consumer360_dw.dim_customer c
        ON f.customer_key =c.customer_key;
    """
    basket_df = pd.read_sql(query_mba, engine)

    top_items = (
        basket_df['item_name']
        .value_counts()
        .head(30)      # keep top 50 items
        .index
    )
    basket_df_filtered = basket_df[
        basket_df['item_name'].isin(top_items)]

    basket = (
        basket_df_filtered
        .groupby(['customer_id', 'item_name'])
        .size()
        .unstack(fill_value=0)
    )

    basket = basket.map(lambda x: 1 if x > 0 else 0)

    frequent_itemsets = apriori(
        basket,
        min_support=0.03,
        use_colnames=True
    )

    rules = association_rules(
        frequent_itemsets,
        metric="lift",
        min_threshold=1
    )

    strong_rules = rules[
        (rules['confidence'] >= 0.6) &
        (rules['lift'] >= 1.1) &
        (rules['support'] >= 0.02)
    ].sort_values(by='lift', ascending=False)

    strong_rules = strong_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
    strong_rules['antecedents'] = strong_rules['antecedents'].astype(str)
    strong_rules['consequents'] = strong_rules['consequents'].astype(str)

    strong_rules.to_sql(
        'market_basket_rules',
        engine,
        if_exists='replace',
        index=False
    )
    logging.info("Market Basket Analysis completed")
    # -------------------------
    # 7. WEEKLY SALES SUMMARY
    # -------------------------
    logging.info("Creating weekly sales summary")
    sales_df['week'] = sales_df['order_date'].dt.to_period('W')

    weekly_sales = (
        sales_df
        .groupby('week')
        .agg(
            total_orders=('order_id', 'nunique'),
            total_revenue=('total_price', 'sum')
        )
        .reset_index()
    )

    weekly_sales.to_sql(
        'weekly_sales_summary',
        engine,
        if_exists='replace',
        index=False
    )
    logging.info("Weekly sales summary created")
    # -------------------------
    # 8. EXPORT FOR POWER BI
    # -------------------------
    EXPORT_PATH ="D:/consumer360_project/powerbi_data/"
    os.makedirs(EXPORT_PATH, exist_ok=True)

    rfm.to_csv(EXPORT_PATH + "rfm_customer_scores.csv", index=False)
    strong_rules.to_csv(EXPORT_PATH + "market_basket_rules.csv", index=False)
    weekly_sales.to_csv(EXPORT_PATH + "weekly_sales_summary.csv", index=False)

    # -----------------------------------------
    # PIPELINE COMPLETED
    # -----------------------------------------
    logging.info("===== Weekly Pipeline Completed Successfully =====")

except Exception as e:
    logging.error("Pipeline execution failed", exc_info=True)
