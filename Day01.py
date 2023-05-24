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