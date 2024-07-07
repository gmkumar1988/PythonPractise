# import pandas as pd
# import yfinance as yf
# import matplotlib.pyplot as plt
# from datetime import datetime
# startdate = datetime.now() - pd.DateOffset(months=3)
# enddate = datetime.now()
# tickers = ['MSFT','GOOG','AAPL','META','NFLX']
# df_list = []
# for ticker in tickers:
#     data = yf.download(ticker,startdate, enddate)
#     df_list.append(data)
# df = pd.concat(df_list,keys=tickers,names=['Tickers','Dates'])
# # print(df.head())
# df = df.reset_index()
# print(df.head())
# print(df.columns)
# import plotly.express as px
# fig = px.area(df,x='Dates',
#               y='Close',
#               color='Tickers',
#               labels={'Date':'Date','Close':'Closing Price','Ticker':'Company'},
#               title='Stock Price Trend Information for Microsoft, Google, Apple, Netflix')
# fig.show()



import matplotlib.pyplot as plot
import pandas as pd
import plotly.express
import statsmodels.api as stats
import numpy as np
insurance_df = pd.read_csv('/Users/maheshg/Downloads/Learner Files - Data Science and ML Fundamentals/2 - Regression/auto_insurance_sweden.csv')

insurance_df.shape

print(insurance_df.head())

###Visualisation of the data

# plot.scatter(insurance_df.claims,insurance_df.payment)
# plot.xlabel("Claims")
# plot.ylabel("Payment[100K Kroner]")
# plot.show()

y_insurance = insurance_df.payment
x_insurance = stats.add_constant(insurance_df['clams'])

model_insurance = stats.OLS(y_insurance,x_insurance)
results_insurance = model_insurance.fit()