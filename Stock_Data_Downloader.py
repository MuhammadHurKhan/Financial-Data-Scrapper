#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Data Downloader")

# create a form for the user to enter the stock ticker and date range
st.subheader("Enter the stock ticker and date range:")
ticker = st.text_input("Ticker")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

# create a button to download the data
if st.button("Download Data as CSV"):
    # download the data and save it to a CSV file
    data = yf.download(ticker, start=start_date, end=end_date)
    filename = f"{ticker}_{start_date}_{end_date}.csv"
    data.to_csv(filename)
    st.success(f"Data downloaded to {filename}.")

# display the data in a table
if st.button("Show Data"):
    data = yf.download(ticker, start=start_date, end=end_date)
    st.write(data)

