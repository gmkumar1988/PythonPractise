###Importing Required Packages and Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as stats

#Reading the datafile
insurance_df = pd.read_csv("/Users/maheshg/Downloads/SwedishMotorInsurance.csv")

print(insurance_df.shape)
#Assessing the data:
insurance_df.head()
print(insurance_df.head(n= 10))
print(insurance_df['Claims'])
#
# insurance_df_new = insurance_df['Claims'],['Payments']
# print(insurance_df_new)
# insurance_df_new.head()

###Visualizing the data
plot.scatter(insurance_df.Claims,insurance_df.Payment)
plot.xlabel('Claims')
plot.ylabel('Payment[100k Kroner]')
plot.show()

###Fitting the regression model :
y_insurance = insurance_df.Payment
x_insurance = stats.add_constant(insurance_df['Claims'])

model_insurance = stats.OLS(y_insurance,x_insurance)
result_insurance = model_insurance.fit()

print(result_insurance.summary())

###Plotting the results:
plot.scatter(insurance_df.Claims, insurance_df.Payment, label = 'Observered')
# plot.show()


# #Plot Combind Chart:
plot.xlabel("Claims")
plot.ylabel("Payment [100k Kroner]")
plot.legend()
plot.show()