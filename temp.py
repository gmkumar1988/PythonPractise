import numpy as np
# a = np.array([1,2,3])
#
# a = 2
# #a+ = 3
# print(a)
#
#
# print(type(a))


###
##import psycopg2 

import pandas as pd
# df = pd.read_csv('/Users/maheshg/Downloads/Python-Projects-Detecting-Fake-News/Data/news.csv')
#
# print(df)
#
#
# import pandas as pd
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# import mlflow
# import mlflow.sklearn
# from mlflow.models.signature import infer_signature
#
#
# iris = datasets.load_iris()
# iris_train = pd.DataFrame(iris.data, columns=iris.feature_names)
# clf = RandomForestClassifier(max_depth=7, random_state=0)
# clf.fit(iris_train, iris.target)
# # Infer the signature from the training dataset and model's predictions
# signature = infer_signature(iris_train, clf.predict(iris_train))
# # Log the scikit-learn model with the custom signature
# mlflow.sklearn.log_model(clf, "iris_rf", signature=signature)


def main(csv_file):
    # read data
    df = get_data(csv_file)

    # split data
    X_train, X_test, y_train, y_test = split_data(df)


# function that reads the data
def get_data(path):
    df = pd.read_csv(path)

    return df


# function that splits the data
def split_data(df):
    X, y = df[['Pregnancies', 'PlasmaGlucose', 'DiastolicBloodPressure', 'TricepsThickness',
               'SerumInsulin', 'BMI', 'DiabetesPedigree', 'Age']].values, df['Diabetic'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    return X_train, X_test, y_train, y_test