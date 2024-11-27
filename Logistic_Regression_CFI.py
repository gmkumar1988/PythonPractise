#Basics Required Packages:
import  pandas as pd
import numpy as np

#Visualization
import matplotlib.pyplot as plot
import seaborn as sns
import matplotlib.pyplot as plt

#SKLearn ML
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

#Loading Dataset
social_network_ads = pd.read_csv("/Users/maheshg/Library/CloudStorage/OneDrive-Microsoft365/Course Files - Classification/2 - Logistic Regression/Social_Network_Ads.csv")

#Displaying the loaded dataframe:
print(social_network_ads)
#Exploring the dataset:
print(social_network_ads.dtypes)
print(social_network_ads.shape)
print(social_network_ads.head())

#Visualization of Exploration of the data:
#plot a histogram of count by age_range, with one series per gender
social_network_ads_bins = social_network_ads[social_network_ads.Age.notna()]

bins = list(range(0,120,10))
social_network_ads_bins['age_range'] = pd.cut(social_network_ads.Age, bins = bins)
chart = sns.catplot(x = "age_range", kind = "count", hue= "Female",
                    data= social_network_ads_bins);
for axes in chart.axes.flat:
    axes.set_xticklabels(axes.get_xticklabels(),rotation = 45)

#Using Sklearn
x_inputs = social_network_ads[['Female','Age','EstimatedSalary']]
y_target = social_network_ads.Purchased

#Splitting into Testing and Training Datasets:
x_train, x_test, y_train, y_test = train_test_split(x_inputs, y_target,train_size=0.8)

#Preprocessing Step (Scaling Data)
x_train = StandardScaler().fit_transform(x_train)
x_test = StandardScaler().fit_transform(x_test)

#Define the classifier
classifier = LogisticRegression(max_iter=1000).fit(x_train, y_train)
print(classifier.score(x_train,y_train))
print(classifier.score(x_test,y_test))

#Make predections on test data:
prediction = classifier.predict(x_test)
print(prediction)

#Plot the confusion matrix
(plot_confusion_matrix(classifier,x_train,y_train))
# ConfusionMatrixDisplay(classifier,x_train,y_train)
