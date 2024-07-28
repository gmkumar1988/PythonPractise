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

m1 = np.array([[2,1],[3,1]])
m2 = np.array([[3,5],[1,1]])
m3 = np.array([[2,3],[4,5]])
determinant_m1_m2_m3 = np.linalg.det(m1*m2*m3)
print(determinant_m1_m2_m3)


