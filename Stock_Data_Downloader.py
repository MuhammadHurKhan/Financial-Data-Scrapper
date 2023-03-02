#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd

# Set page layout and background color
st.set_page_config(page_title="Stock Data Downloader", page_icon=":chart_with_upwards_trend:",
                   layout="wide", page_bg_color="#0D1F30", )

# Add welcome message
st.title("Welcome to Stock Data Downloader!")
st.write("This app allows you to download historical stock price data as a CSV file and view the data in a table and chart. "
         "Please enter a stock ticker symbol and date range to get started.")

# Create a form for the user to enter the stock ticker and date range
st.subheader("Enter the stock ticker and date range:")
ticker = st.text_input("Ticker")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

# Create a button to download the data
if st.button("Download Data as CSV"):
    # Download the data and save it to a CSV file
    data = yf.download(ticker, start=start_date, end=end_date)
    filename = f"{ticker}_{start_date}_{end_date}.csv"
    data.to_csv(filename)
    st.success(f"Data downloaded to {filename}.")

# Create a button to show the data in a table
if st.button("Show Data in Table"):
    data = yf.download(ticker, start=start_date, end=end_date)
    st.write(data)

# Create a button to show the closing price graph
if st.button("Show Closing Price Graph"):
    data = yf.download(ticker, start=start_date, end=end_date)
    fig = pd.DataFrame(data['Close']).plot(title=f"{ticker} Closing Price Since {start_date}",
                                           xlabel="Date", ylabel="Closing Price")
    st.pyplot(fig)

# Create a form for the user to contact me
st.subheader("Contact Me")
form = st.form(key="contact_form")
form.email_input(label="Enter your email address")
form.text_area(label="Enter your message")
form.form_submit_button(label="Submit")

# Enable users to download data since the inception of each stock or index
st.subheader("Download Data Since Inception")
ticker = st.text_input("Enter a stock ticker symbol or index (e.g. AAPL or ^GSPC)")
if st.button(f"Download {ticker} Data Since Inception"):
    data = yf.download(ticker, period="max")
    filename = f"{ticker}_since_inception.csv"
    data.to_csv(filename)
    st.success(f"Data downloaded to {filename}.")
