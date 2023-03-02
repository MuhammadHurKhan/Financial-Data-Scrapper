#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Set background color
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: navy;
        }}
        .sidebar .sidebar-content {{
            background: navy;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and welcome message
st.title("Stock Data Downloader")
st.write("Welcome to Stock Data Downloader! Enter a stock ticker symbol and date range below to get started.")

# Contact form
st.subheader("Contact Me")
form = st.form(key='my_form')
form.email_input(label="Enter your email address")
form.text_area(label="Enter your message")
form.form_submit_button(label="Submit")

# Create a form for the user to enter the stock ticker and date range
st.subheader("Enter the stock ticker and date range:")
ticker = st.text_input("Ticker", "AAPL")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

# Add a checkbox to enable users to download data since the inception of each stock or index
since_inception = st.checkbox("Download data since inception")

# Create a button to download the data
if st.button("Download Data as CSV"):
    if since_inception:
        # download the data since inception and save it to a CSV file
        data = yf.Ticker(ticker).history(period="max")
        filename = f"{ticker}_since_inception.csv"
    else:
        # download the data and save it to a CSV file
        data = yf.download(ticker, start=start_date, end=end_date)
        filename = f"{ticker}_{start_date}_{end_date}.csv"
    data.to_csv(filename, index=False)
    st.success(f"Data downloaded to {filename}.")

# Display the data in a table
if st.button("Show Data"):
    if since_inception:
        # download the data since inception and show it in a table
        data = yf.Ticker(ticker).history(period="max")
    else:
        # download the data and show it in a table
        data = yf.download(ticker, start=start_date, end=end_date)
    st.write(data)

# Show a graph of the closing price since the start date
if start_date:
    if since_inception:
        # download the data since inception and show a graph of the closing price
        data = yf.Ticker(ticker).history(period="max")
    else:
        # download the data and show a graph of the closing price
        data = yf.download(ticker, start=start_date, end=end_date)
    fig = go.Figure(data=go.Scatter(x=data.index, y=data["Close"]))
    fig.update_layout(title=f"{ticker} Closing Price Since {start_date}", xaxis_title="Date", yaxis_title="Closing Price")
    st.plotly_chart(fig)
