# Digital Marketing Performance Analysis

## Overview
This project analyzes historical e-commerce transaction data to evaluate overall business performance and purchasing behavior over time.  
Using order and payment records, the analysis focuses on key performance indicators (KPIs) commonly used in digital marketing and retail analytics.

---

## Objectives
- Analyze completed e-commerce orders and associated payments  
- Evaluate monthly trends in order volume and revenue  
- Assess the stability and behavior of Average Order Value (AOV)  
- Provide high-level, data-driven managerial insights  

---

## Dataset
The analysis is based on publicly available e-commerce data from the **Olist (Brazilian Marketplace)** dataset.

**Main files used:**
- `olist_orders_dataset.csv`
- `olist_order_payments_dataset.csv`

> Note: Due to file size, raw data files are not included in the repository.  
> Please download the datasets and place them in the `data/` folder before running the analysis.

---

## Methodology
1. Data cleaning and preprocessing  
2. Aggregation of payment data at the order level  
3. Merging orders and payments datasets  
4. Calculation of key KPIs:
   - Number of completed orders
   - Total revenue
   - Average Order Value (AOV)
5. Monthly trend analysis and visualization  
6. Filtering of low-volume periods to ensure reliable KPI interpretation  

---

## Key Insights (Summary)
- Revenue growth over time is primarily driven by increases in order volume rather than higher spending per order.  
- Average Order Value remains relatively stable across most months, indicating consistent purchasing behavior.  
- Periods of rapid growth in order volume may coincide with slight declines in AOV, suggesting the acquisition of new or more price-sensitive customers.  

A concise managerial Executive Summary is provided in the `reports/` folder.

---

## Project Structure
- `src/analysis.py` — Analysis scripts
- `figures/` — Output visualizations
- `reports/` — executive summary
- `data/` — Raw datasets (not included)

---

## Tools
- Python (pandas, matplotlib)
- Excel (data inspection and validation)

---

## Author
Parnia Riazat

