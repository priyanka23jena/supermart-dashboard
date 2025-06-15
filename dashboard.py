# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title="Supermart Sales Dashboard")

# Load dataset
df = pd.read_csv('supermart_grocery_sales.csv')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Month'] = df['Order Date'].dt.strftime('%B')
df['Year'] = df['Order Date'].dt.year

st.title("📊 Supermart Grocery Sales Dashboard")

# Sidebar filter
st.sidebar.header("Filter Options")
selected_year = st.sidebar.selectbox("Select Year", sorted(df['Year'].dropna().unique()))

# Filter by year
df_filtered = df[df['Year'] == selected_year]

# Show data
st.subheader(f"📅 Sales Data for {selected_year}")
st.dataframe(df_filtered.head(10))

# Sales by Category
st.subheader("🛒 Sales by Product Category")
category_sales = df_filtered.groupby('Category')['Sales'].sum().sort_values()
st.bar_chart(category_sales)

# Sales by Region
st.subheader("🌍 Sales by Region")
region_sales = df_filtered.groupby('Region')['Sales'].sum()
st.bar_chart(region_sales)

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
monthly_sales = df_filtered.groupby('Month')['Sales'].sum()
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
monthly_sales = monthly_sales.reindex(month_order)
st.line_chart(monthly_sales)
