import pandas as pd
import numpy as np
# 
# list = pd.Series({
#   'name':'Mahesh'
# })

record1 = pd.Series({'Name':'Mahesh'})
record2 = pd.Series({'Name':'Mirula'})
record3 = pd.Series({'Name':'Raghavi'})




df = pd.DataFrame([record1,record2,record3])
df

df.head(10)
