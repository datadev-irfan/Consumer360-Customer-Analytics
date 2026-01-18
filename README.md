# Consumer360-Customer-Analytics
## 📌 Consumer360 – Customer Segmentation & CLV Engine
### 🔍 Project Overview

Consumer360 is an end-to-end customer analytics solution designed for a mid-sized e-commerce retailer to identify high-value customers, predict churn risks, and drive data-driven marketing decisions.

This project integrates SQL, Python, Power BI, and Automation to deliver a production-ready analytics pipeline.

### 🎯 Business Objectives

 &nbsp;&nbsp;&nbsp;&nbsp;Identify High-Value (Champion) customers

 &nbsp;&nbsp;&nbsp;&nbsp;Detect Churn Risk customers early

 &nbsp;&nbsp;&nbsp;&nbsp;Analyze customer retention behavior

 &nbsp;&nbsp;&nbsp;&nbsp;Discover product association patterns

 &nbsp;&nbsp;&nbsp;&nbsp;Predict Customer Lifetime Value (CLV)

 &nbsp;&nbsp;&nbsp;&nbsp;Deliver a weekly auto-updating dashboard

### 🏗️ Architecture Overview
 &nbsp;&nbsp;&nbsp;&nbsp;MySQL (Star Schema) <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ <br>
 &nbsp;&nbsp;&nbsp;&nbsp;Python (RFM, Cohort, Market Basket, CLV) <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ <br>
 &nbsp;&nbsp;&nbsp;&nbsp;Views / CSV Outputs <br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ↓ <br>
 &nbsp;&nbsp;&nbsp;&nbsp;Power BI Dashboard <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ <br>
 &nbsp;&nbsp;&nbsp;&nbsp;Weekly Automation (Task Scheduler) <br>

## 📊 Week-wise Implementation
### Week 1 – Data Modeling & SQL

 &nbsp;&nbsp;&nbsp;&nbsp;Designed Star Schema (Fact Sales + Dimensions)

 &nbsp;&nbsp;&nbsp;&nbsp;Implemented surrogate keys

 &nbsp;&nbsp;&nbsp;&nbsp;Created optimized SQL views

 &nbsp;&nbsp;&nbsp;&nbsp;Ensured queries execute efficiently

 &nbsp;&nbsp;&nbsp;&nbsp;Verified ERD and relationships

### Week 2 – Advanced Analytics (Python)

 &nbsp;&nbsp;&nbsp;&nbsp;Implemented RFM Segmentation

 &nbsp;&nbsp;&nbsp;&nbsp;Assigned customer segments (Champion, Loyal, Hibernating)

 &nbsp;&nbsp;&nbsp;&nbsp;Performed Market Basket Analysis using Apriori

 &nbsp;&nbsp;&nbsp;&nbsp;Conducted Cohort Analysis

 &nbsp;&nbsp;&nbsp;&nbsp;Implemented CLV prediction using Lifetimes library

### Week 3 – Power BI Dashboard

 &nbsp;&nbsp;&nbsp;&nbsp;Built interactive dashboard with:

 &nbsp;&nbsp;&nbsp;&nbsp;KPI cards

 &nbsp;&nbsp;&nbsp;&nbsp;RFM visuals

 &nbsp;&nbsp;&nbsp;&nbsp;Cohort heatmap

 &nbsp;&nbsp;&nbsp;&nbsp;Market basket insights

 &nbsp;&nbsp;&nbsp;&nbsp;Implemented Row-Level Security (RLS)

 &nbsp;&nbsp;&nbsp;&nbsp;Designed UX aligned with business use cases

### Week 4 – Automation & Delivery

 &nbsp;&nbsp;&nbsp;&nbsp;Created end-to-end Python automation script

 &nbsp;&nbsp;&nbsp;&nbsp;Scheduled weekly execution using Windows Task Scheduler

 &nbsp;&nbsp;&nbsp;&nbsp;Automated data refresh and dashboard update

 &nbsp;&nbsp;&nbsp;&nbsp;Validated full pipeline execution

📈 Key Insights Delivered

 &nbsp;&nbsp;&nbsp;&nbsp;Champions contribute the highest long-term revenue

 &nbsp;&nbsp;&nbsp;&nbsp;Specific regions show increased churn risk

 &nbsp;&nbsp;&nbsp;&nbsp;Strong product association patterns identified

 &nbsp;&nbsp;&nbsp;&nbsp;CLV enables proactive premium engagement strategies

## 🛠️ Tech Stack

 &nbsp;&nbsp;&nbsp;&nbsp;SQL (MySQL) – Data modeling & views

 &nbsp;&nbsp;&nbsp;&nbsp;Python (Pandas, Lifetimes, mlxtend) – Analytics

 &nbsp;&nbsp;&nbsp;&nbsp;Power BI – Visualization & RLS

 &nbsp;&nbsp;&nbsp;&nbsp;Windows Task Scheduler – Automation

## 📂 Repository Structure

 &nbsp;&nbsp;&nbsp;&nbsp;Refer to the folder structure above for SQL scripts, notebooks, dashboards, and documentation.

## 🚀 Outcome

 &nbsp;&nbsp;&nbsp;&nbsp;Consumer360 enables data-driven customer engagement, retention planning, and revenue optimization with a fully automated analytics pipeline.

### 👤 Author

### Mohamed Irfan
### Data Analytics Intern – Zaalima Development Pvt. Ltd.
