#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd

# Set page config
st.set_page_config(page_title="Stock Data Downloader", page_icon=":money_with_wings:", layout="wide")

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: #001F3F;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add welcome note
st.title("Welcome to the Stock Data Downloader!")
st.write("This app allows you to download historical stock data and create visualizations.")

# Create a form for the user to enter the stock ticker and date range
with st.form("user_inputs"):
    ticker = st.text_input("Enter the stock ticker (e.g., AAPL)")
    start_date = st.date_input("Enter the start date")
    end_date = st.date_input("Enter the end date")
    email = st.text_input("Enter your email address")
    submit_button = st.form_submit_button(label="Download Data")

if submit_button:
    # download the data and save it to a CSV file
    data = yf.download(ticker, start=start_date, end=end_date)
    filename = f"{ticker}_{start_date}_{end_date}.csv"
    data.to_csv(filename)
    st.success(f"Data downloaded to {filename}.")

    # send an email with the download link
    body = f"Here is the download link for {filename}: {st.get_static_download_link(filename)}"
    subject = f"Stock Data Download: {filename}"
    st.write(f"Sending email to {email}...")
    st.write(f"Subject: {subject}")
    st.write(f"Body: {body}")

# Display the data in a table and plot
if ticker and start_date and end_date:
    data = yf.download(ticker, start=start_date, end=end_date)
    st.subheader(f"{ticker} Historical Data ({start_date} to {end_date})")
    st.write(data)

    # create a plot showing the closing price
    chart_data = data.reset_index()
    chart_data = chart_data[["Date", "Close"]]
    chart_data = chart_data.set_index("Date")
    st.line_chart(chart_data, use_container_width=True)
