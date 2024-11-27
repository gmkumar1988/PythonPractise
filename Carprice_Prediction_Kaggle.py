###Importing Required Packages and Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as stats
import statsmodels.regression.linear_model

#Reading the datafile
carprice_df = pd.read_csv("/Users/maheshg/Dropbox/Sample Datasets Kaggle/car_price_prediction.csv")

# ##Understanding the shape of the dataset :
print(carprice_df.shape)
#
# #Viewing the first head of the rows in the dataset:
print(carprice_df.head(n= 20))
#
# ###Splitting the dataset into two chunks : Test and Training
# #We will train the model 70% of the data and test is results on the remaining 30%.
train_df = carprice_df.sample(frac=0.7, random_state=99)
test_df = carprice_df.drop(train_df.index)
print(train_df.columns)
#
# Visualize the train and test dataset split value:
# print(train_df.shape)
# print(test_df.shape)

###Ploting the trained dataset Engine Volume vs Price of the trained dataset:
# plot.scatter(train_df['Prod. year'], train_df['Price'])
# plot.xlabel('Engine Volume')
# plot.ylabel('Price')
# plot.show()

y_train = train_df['Price']
x_train = stats.add_constant(train_df['Mileage'])
# model_carprice = stats.OLS(y_train,x_train)
# print(model_carprice)
# print(train_df.columns)

#Converting all the values to numeric especially the newly added constant to x variable:
x_train['Mileage'] = pd.to_numeric(x_train['Mileage'], errors= 'coerce')
data = np.asarray(x_train)
print(data)
#
# model_carprice = stats.OLS(y_train,x_train)

#Checking for NAs
print(x_train.isna().sum())

#Check for infinite values :
print(np.isinf(x_train).sum())
print(np.isinf(y_train).sum())
#Drop or replace NA values
x_train = x_train.replace([np.inf, -np.inf], np.nan).dropna()
y_train = y_train.replace([np.inf, -np.inf], np.nan).dropna()


model_carprice = stats.OLS(y_train,x_train)
