import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Modern ETL Pipeline Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Modern ETL Pipeline Dashboard")

engine = create_engine(
    "postgresql+psycopg2://admin:admin123@127.0.0.1:5433/warehouse"
)

df = pd.read_sql("SELECT * FROM gold_metrics", engine)

st.subheader("Gold Metrics")

st.dataframe(df, use_container_width=True)

st.subheader("Revenue by Event Type")

st.bar_chart(df.set_index("event_type")["total_revenue"])

st.subheader("Total Events")

st.bar_chart(df.set_index("event_type")["total_events"])