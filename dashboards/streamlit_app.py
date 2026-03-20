import pandas as pd
import streamlit as st

df = pd.read_parquet("data/processed/events")

st.title("Netflix Member Insights Dashboard")

st.metric("Total Events", len(df))
st.metric("Unique Users", df["user_id"].nunique())

st.line_chart(df.groupby("timestamp").size())
