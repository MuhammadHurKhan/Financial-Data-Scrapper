#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf
import streamlit as st
import base64

# Define function to download stock data
@st.cache
def download_data(ticker, start_date, end_date):
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start_date_str, end=end_date_str)
    return data

# Define main function for app
def main():
    # Set page title and icon
    st.set_page_config(page_title='Stock Data Downloader', page_icon=':chart_with_upwards_trend:')
    
    # Define sidebar inputs
    st.sidebar.title('Stock Data Downloader')
    ticker = st.sidebar.text_input('Enter Ticker Symbol (e.g. AAPL)')
    start_date = st.sidebar.date_input('Enter Start Date', value=pd.to_datetime('2010-01-01'))
    end_date = st.sidebar.date_input('Enter End Date', value=pd.to_datetime('today'))
    
    # Define welcome message
    st.write('Welcome to the Stock Data Downloader! Please wait while we retrieve your data...')
    
    # Download data and show table
    try:
        data = download_data(ticker, start_date, end_date)
        st.write(data)
    except Exception as e:
        st.write('An error occurred while retrieving the data. Please try again later.')
        st.write('Error Details:', e)

if __name__ == '__main__':
    main()
# Allow the user to download the data in a CSV file format
csv = data.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="{ticker}.csv">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)

