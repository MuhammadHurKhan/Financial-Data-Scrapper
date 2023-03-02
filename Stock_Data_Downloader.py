#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf
import streamlit as st
import base64

# Create a Streamlit application
st.title("Stock Data Downloader")

# Get the ticker symbol and time period from the user
ticker = st.text_input("Enter the ticker symbol for the desired stock or index (e.g., AAPL, ^GSPC):")
start_date = st.date_input("Enter the start date for the desired time period:")
end_date = st.date_input("Enter the end date for the desired time period:")

# Convert the start and end dates to strings
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

# Retrieve the data for the specified stock or index and time period
data = yf.download(ticker, start=start_date_str, end=end_date_str)

# Remove the timezone information from the datetime index
data.index = data.index.tz_localize(None)

# Display the data in a table
st.write(data)

# Allow the user to download the data in a CSV file format
csv = data.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="{ticker}.csv">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)

