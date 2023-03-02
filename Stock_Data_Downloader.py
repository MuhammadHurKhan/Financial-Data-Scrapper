#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import yfinance as yf
import pandas as pd
import base64

# Set page title and favicon
st.set_page_config(page_title="Stock Data Downloader", page_icon=":money_with_wings:")

# Set some custom CSS styles
st.markdown("""
<style>
h1, h2, h3 {
    color: #000080.;
}
.btn-primary {
    background-color: #3366FF;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Render the page
st.title("Stock Data Downloader")
st.subheader("Enter the stock ticker and date range:")

# Create a form for the user to enter the stock ticker and date range
ticker = st.text_input("Ticker")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

# Create a button to download the data
if st.button("Download Data as CSV", key="download"):
    # Download the data and save it to a CSV file
    data = yf.download(ticker, start=start_date, end=end_date)
    filename = f"{ticker}_{start_date}_{end_date}.csv"
    data.to_csv(filename)
    st.success(f"Data downloaded to {filename}.")
    
    # Create a download link for the CSV file
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV</a>'
        st.markdown(href, unsafe_allow_html=True)

# Display the data in a table
if st.button("Show Data", key="show"):
    data = yf.download(ticker, start=start_date, end=end_date)
    st.write(data)
    
   # Display a line chart of the closing price
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="Closing Price"))
    fig.update_layout(title=f"{ticker} Closing Price", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)

