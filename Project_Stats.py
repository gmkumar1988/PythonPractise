import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
startdate = datetime.now() - pd.DateOffset(months=3)
enddate = datetime.now()
tickers = ['MSFT','GOOG','AAPL','META','NFLX']
df_list = []
for ticker in tickers:
    data = yf.download(ticker,startdate, enddate)
    df_list.append(data)
df = pd.concat(df_list,keys=tickers,names=['Tickers','Dates'])
# print(df.head())
df = df.reset_index()
print(df.head())
print(df.columns)
import plotly.express as px
fig = px.area(df,x='Dates',
              y='Close',
              color='Tickers',
              labels={'Date':'Date','Close':'Closing Price','Ticker':'Company'},
              title='Stock Price Trend Information for Microsoft, Google, Apple, Netflix')
fig.show()