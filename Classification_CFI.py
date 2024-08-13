#Basics Required Packages:
import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np

#Visualization
import matplotlib.pyplot as plot
import seaborn as sns

#Sklearn ML General
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
# from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay


from sklearn import metrics

#Sklearn ML Algorithms
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
# from sklearn import SVM
from sklearn.svm import SVC, SVR

#Data Exploration
employee_data = pd.read_csv("/Users/maheshg/Library/CloudStorage/OneDrive-Microsoft365/Course Files - Classification/3 - Classification Algorithms/HREmployeeData.csv")
print(employee_data)

#Data Exploration
print(employee_data.describe())

#Plot a histogram of the target variable
employee_data.Attrition.value_counts().nlargest(40).plot(kind = 'bar',figsize = (10,5))
plt.title('Attrition of the employees')
plt.ylabel('Occurence of each in the dataset')
plt.xlabel('Attrition')

#Predictive Modelling :
x_inputs = employee_data.drop(['Attrition'], axis = 1)
y_target = employee_data['Attrition']

#Spliting test and train dataset:
x_train,x_test, y_train, y_test = train_test_split(x_inputs, y_target,
                                                   test_size=0.5,random_state=0)

#Define the classifiers :
classifier = {
    "classifier_NB": GaussianNB(),
    "classifier_SVM": SVC(gamma=2, C = 1),
    "classifier_KNN": KNeighborsRegressor(n_neighbors=3),
    "classifier_DT": DecisionTreeClassifier(random_state=0),
    "classifier_RT": RandomForestClassifier(max_depth=2, random_state=0)
}
results = {}
print("Number of mislabeled points out of total %d points:" % x_test.shape[0])

for clf_name, clf_model in classifier.items():
    clf_model.fit(x_train,y_train)
    clf_model.predict(x_test)
    print(clf_name + ": %d" % (y_test != clf_model.predict(x_test)).sum())
    results [clf_name] = clf_model.predict(x_test)