import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels as sm
desired_width=500
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns',10)
import seaborn as sns
sns.set_theme(style= 'darkgrid')
car_data = pd.read_csv('/Users/maheshg/Dropbox/Sample Datasets Kaggle/CarPrice_Assignment.csv')
print(car_data.head())
plt.figure(figsize= (12,8))
# sns.regplot(data = car_data, x = 'curbweight', y= 'price')
# plt.title('CurbWeight vs Price')
sns.boxplot(data = car_data, x = 'carbody', y = 'price')
plt.title('Carbody vs Price')
plt.show()