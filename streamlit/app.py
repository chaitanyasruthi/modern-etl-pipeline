import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Modern ETL Pipeline Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Modern ETL Pipeline Dashboard")

# Load Gold Metrics from CSV
df = pd.read_csv("streamlit/gold_metrics.csv")

# Display table
st.subheader("📋 Gold Metrics")
st.dataframe(df, use_container_width=True)

# Revenue Chart
st.subheader("💰 Revenue by Event Type")
st.bar_chart(
    df.set_index("event_type")["total_revenue"]
)

# Events Chart
st.subheader("📈 Total Events")
st.bar_chart(
    df.set_index("event_type")["total_events"]
)

# Footer
st.success("✅ ETL Pipeline Executed Successfully")