import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Modern ETL Pipeline Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Modern ETL Pipeline Dashboard")

# Read data from CSV instead of PostgreSQL
df = pd.read_csv("streamlit/gold_metrics.csv")

st.subheader("Gold Metrics")
st.dataframe(df, use_container_width=True)

st.subheader("Revenue by Event Type")
st.bar_chart(df.set_index("event_type")["total_revenue"])

st.subheader("Total Events")
st.bar_chart(df.set_index("event_type")["total_events"])
