import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,PolynomialFeatures,OneHotEncoder
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import cross_val_score,train_test_split
medical_cost = pd.read_csv("/Users/maheshg/Library/CloudStorage/OneDrive-Microsoft365/Sample Datasets Kaggle/medical_insurance.csv")
medical_cost.head()
medical_cost.replace('?',np.nan, inplace=True)
medical_cost.info()
#Smoker is identified as categorical variable, replace with most frequency entry
is_smoker = medical_cost['smoker'].value_counts().idxmax()
medical_cost["smoker"].replace(np.nan,is_smoker, inplace=True)
# print(is_smoker)
#Age is continuous variable, replace with mean age
mean_age = medical_cost["age"].astype(float).mean(axis=0)
medical_cost["age"].replace(np.nan,mean_age,inplace=True)
#Update Data type for Age:
medical_cost["age"] = medical_cost["age"].astype(int)
# medical_cost["smoker"] = medical_cost["smoker"].astype(int)
print(medical_cost.head(10))
medical_cost["charges"] = np.round(medical_cost["charges"],2)
print(medical_cost.head(5))
###Exploratory Analysis : Implementing the regression analysis
# sns.regplot(x = "bmi", y = "charges",
#             data = medical_cost, line_kws={"color":"red"})
# plt.ylim(0,)

###Exploratory Analysis : Implementing the box plot w.r.t Smoker:
sns.boxplot(x= "smoker",y="charges",
            data = medical_cost)
# plt.show()
###Fitting a linear regression model : (Model Development):
x = medical_cost["smoker"]
y = medical_cost["charges"]

#Create transformer for one hot encoding the "smoker" column:
preprocessor = ColumnTransformer(
    transformers=[('smoker', OneHotEncoder(), ['smoker'])],
    remainder='passthrough'
)


# ###Create Pipeline with transformer and linear regression model
# model = Pipeline(steps=[('preprocessor', preprocessor),
#                         ('regressor', LinearRegression())])
#
# model.fit(x,y)
# print(model.score(x,y))


#create a new dataframe with one-hot encoded categorical variables
z= pd.get_dummies(medical_cost[["age","sex",
                                "bmi","children",
                                "smoker","region"]])

#initialize the linear regression model
lm =LinearRegression()
lm.fit(z,y)
print(lm.score(z,y))


#create a training pipeline that uses StandardScaler(), PolynomialFeatures() and LinearRegression()
#to create a model that can predict the charges value using all the other attributes of the dataset.

# Y and Z use the same values as defined in previous cells
Input =[('scale',StandardScaler()),('polynomial',
                                   PolynomialFeatures(include_bias=False)),('model',
                                                                          LinearRegression())]
pipe = Pipeline(Input)
z = z.astype(float)
pipe.fit(z,y)
ypipe =pipe.predict(z)

#print  R^2 score
print(r2_score(y,ypipe))

