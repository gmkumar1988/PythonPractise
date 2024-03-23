# # check scikit-learn version
# import sklearn
# print(sklearn.__version__)
#
# #example of multioutput regression
# from sklearn.datasets import make_regression
# ###create datasets
# X,y = make_regression(n_samples=1000,n_features=10,
#                       n_informative=5,n_targets=2,
#                       random_state=1)
# ###Summarise Dataset
# print(X.shape, y.shape)
#
# ###Linear Regression
# from sklearn.datasets import make_regression
# from sklearn.linear_model import LinearRegression
#
# ###create datasets
# x,y = make_regression(n_samples=1000,n_features=10,
#                       n_informative=5,n_targets=2,
#                       random_state=1,noise=0.5)
# print(x.shape, y.shape)
# #defining the model
# model = LinearRegression()
# #fitting the model
# model.fit(x,y)
# ###make a prediction
# row = [0.21947749, 0.32948997, 0.81560036, 0.440956, -0.0606303, -0.29257894, -0.2820059, -0.00290545, 0.96402263, 0.04992249]
# yhat = model.predict([row])
# print("value of yhat is :",yhat)
# ####
#
#Example 1 : Regression of Auto cars:
import pandas as pd
import matplotlib.pyplot as plt
medical_cost = pd.read_csv("/Users/maheshg/Library/CloudStorage/OneDrive-Microsoft365/Sample Datasets Kaggle/medical_insurance.csv")
medical_cost.head()

print(medical_cost.head())
plt.figure(figsize=(10,10))
plt.scatter(medical_cost['age'],medical_cost['charges'])
# plt.bar(medical_cost[medical_cost'smoker'],medical_cost['charges'])
plt.title("Medical Cost Details Based on Age and Charges")
plt.xlabel("Age Details")
plt.ylabel("Charges")
plt.show()