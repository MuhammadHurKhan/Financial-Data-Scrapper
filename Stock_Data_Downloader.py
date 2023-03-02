#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd
import base64

# Set page layout and background color
st.set_page_config(page_title="Stock Data Downloader", page_icon=":chart_with_upwards_trend:", layout="wide", page_bg_color="#0D1F30")

# Add welcome message
st.title("Welcome to Stock Data Downloader!")
st.write("This app allows you to download historical stock price data as a CSV file and view the data in a table and chart. Please enter a stock ticker symbol and date range to get started.")

# Create a form for the user to enter the stock ticker and date range
st.subheader("Enter the stock ticker and date range:")
ticker = st.text_input("Ticker")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

# Create a button to download the data
if st.button("Download Data as CSV"):
    # Download the data and save it to a CSV file
    data = yf.download(ticker, start=start_date, end=end_date)
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    filename = f"{ticker}_{start_date}_{end_date}.csv"
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download Data as CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

# Create a button to show the data in a table
if st.button("Show Data in Table"):
    data = yf.download(ticker, start=start_date, end=end
