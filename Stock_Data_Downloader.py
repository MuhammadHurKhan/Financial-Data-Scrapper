#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd
import smtplib

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
form = st.form(key="contact_form")
email = form.email_input(label="Enter your email address")
message = form.text_area(label="Enter your message")
if form.form_submit_button(label="Submit"):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email_address", "your_email_password")
        server.sendmail("your_email_address", email, message)
        server.quit()
        st.success("Message sent!")
    except Exception as e:
        st.error("Unable to send message.")
        st.exception(e)
# Enable users to download data since the inception of each stock or index
st.subheader("Download Data Since Inception")
ticker_since = st.text_input("Enter a stock ticker symbol or index (e.g. AAPL or ^GSPC)")
if st.button(f"Download {ticker_since} Data Since Inception"):
    data_since = yf.download(ticker_since, period="max")
    filename_since = f"{ticker_since}_since_inception.csv"
    data_since.to_csv(filename_since)
    st.success(f"Data downloaded to {filename_since}.")
