# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed May 24 18:30:13 2023
#
# @author: maheshg
# """
#
# from statistics import median
# from statistics import mean
# from math import isnan
# from itertools import filterfalse
#
# data = [20.7, float('NaN'), 19.2, 18.3, float('NaN'),14,4]
#
# sorted(data)
#
# median(data)
# print(median(data))
#
# mean(data)
#
# print(mean(data))
#
# clean = list(filterfalse(isnan, data))
#
# sorted(clean)
#
# median(clean)
#
# mean([1,2,3,4,5,8,9])
#
# # from fractions import Fraction as F
# #
# # mean([F(3,7),F(1,21),F(5,3),F(1,3)])
# #
# #
# #
# # # import pip
# # # pip.main(['install','seaborn'])
# #
# # import pandas as pd
# #
# # import seaborn as sns
#
#
# from azure.ai.ml.entities import Data
# from azure.ai.ml.constants import AssetTypes
#
# my_path = '<supported-path>'
#
# my_data = Data(
#     path=my_path,
#     type=AssetTypes.URI_FILE,
#     description="<description>",
#     name="<name>",
#     version="<version>"
# )

# ml_client.data.create_or_update(my_data)


# import matplotlib.pyplot as plt
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.layers import Dense,Input
# from tensorflow.keras import Sequential
# from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy
# from tensorflow.keras.activations import sigmoid
# # from lab_utils_common import dlc
# x = np.array([200.0,17.0])
# layer_1 = Dense(units = 3, activation = 'sigmoid')
# a1 = layer_1(x)


# import tensorflow as tf
# model = Sequent