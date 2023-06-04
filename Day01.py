#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:30:13 2023

@author: maheshg
"""

from statistics import median
from statistics import mean
from math import isnan
from itertools import filterfalse

data = [20.7, float('NaN'), 19.2, 18.3, float('NaN'),14,4]

sorted(data)

median(data)
print(median(data))

mean(data)

print(mean(data))

clean = list(filterfalse(isnan, data))

sorted(clean)

median(clean)

mean([1,2,3,4,5,8,9])

from fractions import Fraction as F

mean([F(3,7),F(1,21),F(5,3),F(1,3)])



# import pip 
# pip.main(['install','seaborn'])

import pandas as pd

import seaborn as sns


