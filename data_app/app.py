import streamlit as st
import pandas as pd

st.title("Business Data Analyzer")
st.write("Upload your business data to analyze it.")

file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if file is not None:
    st.success("File uploaded successfully!")

    # Read file
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Show data
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # KPIs
    st.subheader("Key Metrics")
    col1, col2 = st.columns(2)

    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))

    # Charts
    st.subheader("Data Visualization")
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        st.bar_chart(df[numeric_cols].head(10))
    else:
        st.write("No numeric columns to plot")

    # Insights
    st.subheader("Insights")

    if len(numeric_cols) > 0:
        highest_col = df[numeric_cols].sum().idxmax()
        st.write(f"Highest contributing column: {highest_col}")