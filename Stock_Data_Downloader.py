#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import base64

# Set page title and favicon
st.set_page_config(page_title="Stock Data Downloader", page_icon=":money_with_wings:")


# Set some custom CSS styles
st.markdown("""
    <style>
        body {
            background-color: #001f3f !important;
            color: #FFFFFF;
        }
        
        h1, h2, h3 {
            color: #FFFFFF;
        }

        .btn-primary {
            background-color: #191970;
            color: #FFFFFF;
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

# Add your information to the app
st.markdown("""


## About Me
My name is Muhammad Hur Khan, and I'm on a mission to help businesses achieve their goals through data analysis and financial modeling. With a keen eye for business process analysis and optimization, I'm dedicated to finding ways to drive your business growth and take you to the next level.

As an experienced operational assistant and accounting analyst, I've helped companies identify new business opportunities and increase their revenue, while streamlining their processes and improving performance. I'm proficient in Power BI and other CRM tools, and I'm always ready to dive into your data to uncover insights that can help you make informed decisions and drive your business forward.

With a degree in Computational Finance from NED University of Engineering and Technology and certifications in EFSET English and Power BI, I'm a skilled communicator and a creative problem solver. I know how to analyze financial data and make it accessible and understandable to non-experts, so you can make informed decisions and achieve your business goals.

If you're looking for a data analyst who can help you optimize your business, then let's connect! I'm eager to hear about your business and your goals, and I'm ready to bring my expertise to help you succeed.
""")


