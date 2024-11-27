# name = input("Enter:")
# # print(name)
# apple = input('Enter:')
# # x = apple - 10
# x = int(apple) - 10
# # print(x)
# fruit = 'banana'
# letter = fruit[1]
# print(letter)
# x = 3
# w = fruit[x-1]
# print(w)
# zot = 'abc'
# print(zot[5])
import numpy as np

fruit = 'banana'
print(len(fruit))
# index = 0
# while index <len(fruit):
#     letter = fruit[index]
#     print(index,letter)
#     index = index + 1
#
# for letter in fruit:
#     print(letter)
# # word = 'banana'
# # count = 0
# # for letter in word:
# #     if letter == 'a':
# #         count = count + 1
# #         print(count)
#
#
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])
#
# a = [1,32,5,623]
# print(a [:2])
#
# print(a [2:4])
#
# b = np.array([[1,2,3,5], [24,52,52,21] , [232,4232,123,3123]])
#
# print(b[:2])
#
# import re
#
# text = "This is Mirula"
#
# if re.search("is",text):
#     print("wonderful")
# else:
#     print("bye")
# print(re.findall("mirula",text))
#
# text = "Mirula works differently. Mirula getsw good grades, Our student Amy is successful Mirula"
# print(re.split("Mirula",text))
# print(re.findall("Mirula",text))
#
# print(re.search("Mirula",text))
#
# grades = "ACAAADB"
# print(re.findall("B",grades))
#
# print(re.findall("[AB]",grades))
# print(re.findall("[A],[B-D]",grades))
# print(re.findall("AB|AC",grades))
# print(re.findall("A{2,10}",grades))
# print(re.findall("A{1,1}A{1,1}",grades))
#
# import re
#
# string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
# result = re.findall('b[ao]t', string)
# print(result)
#
# def l2_dist(a, b):
#     result = ((a - b) * (a - b)).sum()
#     result = result ** 0.5
#     return result
#
#
#
# a1 = np.random.rand(4)
# a2 = np.random.rand(4, 1)
# a3 = np.array([[1, 2, 3, 4]])
# a4 = np.arange(1, 4, 1)
# a5 = np.linspace(1 ,4, 4)
#
# print(a5.shape == a1.shape)
#
#
# import numpy as np
#
# old = np.array([[1, 1, 1], [1, 1, 1]])
# new = old
# new[0, :2] = 0
#
# print(old)
#
#
#
# import re
# s = 'ACAABAACAAAB'
# result = re.findall('A{1,2}', s)
# L = len(result)
# print(L)

#Introduction to pandas:
import pandas as pd
students = ['Alice','Jack','Molly']
print(pd.Series(students))

numbers = [1,2,3]
print(pd.Series(numbers))

students = ['Alice','Jack','None']
print(pd.Series(students))

numbers = [1,2,None]
print(pd.Series(numbers))

import numpy as np
print(np.nan == None)
print(np.nan == np.nan)

print(np.isnan(np.nan))

students_scores = {'Alice' : 'Physics',
                   'Jack':'Chemistry',
                   'Molly':'English'}
print(pd.Series(students_scores))
