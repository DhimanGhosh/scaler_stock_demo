import streamlit as st
import yfinance as yf
import datetime


st.title('Welcome to Stock Market')


ticker_symbol = st.text_input('Enter stock symbol', 'AAPL')
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input('Please enter starting date', datetime.date(2019, 1, 1))
with col2:
    end_date = st.date_input('Please enter ending date', datetime.date(2022, 12, 31))
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(
    start=start_date,
    end=end_date
)

# st.dataframe(ticker_df)

col1, col2 = st.columns(2)
with col1:
    st.write('# Daily Closing Price')
    st.line_chart(ticker_df['Close'])
with col2:
    st.write('# Highest Price')
    st.line_chart(ticker_df['High'])
