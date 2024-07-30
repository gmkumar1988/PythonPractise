import os
import shutil
# import psutil
# # print('-os:')
# # print(dir(os))
# print('shutil:')
# # print(dir(shutil))
# # print('psutil')
# # print(dir(psutil))
# print(psutil.process_iter())
#
# from pprint import pprint
# print('Disk Partition')
# pprint(psutil.disk_partitions())
# # pprint(psutil.disk_usage())

# matrix = [[1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]]
#
# print("Matrix =", matrix)

import numpy as np
# a = np.array([[1,2],[3,4]])
# print(np.linalg.det(a))

# b = np.array([[0,0,2],[2,2,1],[1,0,0]])
# print(np.linalg.det(b))
#
# c = (np.linalg.inv(b))
# print(np.linalg.det(c))
#
# m1 = np.array([[2,1],[3,1]])
# m2 = np.array([[3,5],[1,1]])
# m3 = np.array([[2,3],[4,5]])
# determinant_m1_m2_m3 = np.linalg.det(m1*m2*m3)
# print(determinant_m1_m2_m3)

# m = np.array([[1,0,1],[0,1,0],[1,1,1]])
# n = np.array([[2,8,7],[4,3,9],[1,9,5]])
# p = np.dot(m,n)
# print(p)
# q = np.linalg.det(p)
# print(q)
# # np.linalg.det()

# print(np.linalg.det(p))
# import pandas as pd
# df = pd.DataFrame({
# 'A': [1, 2, 2, 3, 4],
# 'B': [5, 6, 7, 8, 9],
# 'C': [1, 1, 1, 1, 1]
# })
# df['A_rank'] = df['A'].rank()
# print(df)

a = np.array([[3,5],[2,8]])
print("Shape of array:\n",np.shape(a))
print("Covariance matrix of a:\n", np.cov(a))
# m = np.array([[1,0,1],[0,1,0],[1,1,1]])
# print("Shape of array:\n",np.shape(m))
# n = np.array([[2,8,7],[4,3,9],[1,9,5]])
# print("Shape of array:\n",np.shape(n))
# print(np.dot(m,n))
# print(np.linalg.det(np.dot(m,n)))