import pandas as pd
import matplotlib.pyplot as plt
import os


# Load datasets
orders = pd.read_csv("../data/olist_orders_dataset.csv", encoding="latin1")
payments = pd.read_csv("../data/olist_order_payments_dataset.csv", encoding="latin1")


# Basic inspection
print("ORDERS SHAPE:", orders.shape)
print("PAYMENTS SHAPE:", payments.shape)

print("\nORDERS INFO:")
orders.info()

print("\nPAYMENTS INFO:")
payments.info()

print("\nORDERS HEAD:")
print(orders.head())

print("\nPAYMENTS HEAD:")
print(payments.head())




# Convert timestamps to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)

# Aggregate payments per order (some orders have multiple payments)
payments_agg = payments.groupby('order_id', as_index=False).agg({
    'payment_value': 'sum'
})

payments_agg.rename(columns={'payment_value': 'revenue'}, inplace=True)

# Join orders with payments
orders_merged = orders.merge(
    payments_agg,
    on='order_id',
    how='left'
)

print("MERGED SHAPE:", orders_merged.shape)
print(orders_merged[['order_id', 'order_status', 'revenue']].head())






# KPI Definition
completed = orders_merged[orders_merged['order_status'] == 'delivered'].copy()

print("COMPLETED ORDERS SHAPE:", completed.shape)

completed['revenue'] = completed['revenue'].fillna(0)


total_orders = completed['order_id'].nunique()
total_revenue = completed['revenue'].sum()
average_order_value = completed['revenue'].mean()

print("Total completed orders:", total_orders)
print("Total revenue:", round(total_revenue, 2))
print("Average order value:", round(average_order_value, 2))


# Create order month
completed['order_month'] = completed['order_purchase_timestamp'].dt.to_period('M')

monthly_kpis = completed.groupby('order_month').agg(
    orders=('order_id', 'nunique'),
    revenue=('revenue', 'sum')
).reset_index()

print(monthly_kpis.head())





# visualization
os.makedirs("../figures", exist_ok=True)


monthly_kpis = monthly_kpis.copy()
monthly_kpis["order_month"] = monthly_kpis["order_month"].dt.to_timestamp()
monthly_kpis = monthly_kpis.sort_values("order_month")

# AOV
monthly_kpis["aov"] = monthly_kpis["revenue"] / monthly_kpis["orders"]

# Filter low-volume months
monthly_kpis_plot = monthly_kpis[monthly_kpis["orders"] >= 50].copy()
monthly_kpis_plot['aov'] = monthly_kpis_plot['revenue'] / monthly_kpis_plot['orders']


# Orders
plt.figure(figsize=(8,5))
plt.plot(monthly_kpis_plot["order_month"], monthly_kpis_plot["orders"], marker="o")
plt.title("Monthly Number of Completed Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../figures/monthly_orders.png", dpi=300, bbox_inches="tight")
plt.show()



# Revenue
plt.figure(figsize=(8,5))
plt.plot(monthly_kpis_plot["order_month"], monthly_kpis_plot["revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../figures/monthly_revenue.png", dpi=300, bbox_inches="tight")
plt.show()



# AOV
plt.figure(figsize=(8,5))
plt.plot(monthly_kpis_plot["order_month"], monthly_kpis_plot["aov"], marker="o")
plt.title("Average Order Value (AOV) Over Time")
plt.xlabel("Month")
plt.ylabel("Average Order Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../figures/monthly_aov.png", dpi=300, bbox_inches="tight")
plt.show()
