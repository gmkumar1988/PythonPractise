import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
plt.show()
# print(mean_age.head())
# print(medical_cost.head())
# plt.figure(figsize=(10,10))
# plt.scatter(medical_cost['age'],medical_cost['charges'])
# plt.bar(medical_cost[medical_cost'smoker'],medical_cost['charges'])
# plt.plot(medical_cost['age'],(medical_cost['age']/ -100) + 40, c= 'red')
# plt.title("Medical Cost Details Based on Age and Charges")
# plt.xlabel("Age Details")
# plt.ylabel("Charges")
# plt.show()