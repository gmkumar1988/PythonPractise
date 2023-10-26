import os
import shutil
import psutil
# print('-os:')
# print(dir(os))
print('shutil:')
# print(dir(shutil))
# print('psutil')
# print(dir(psutil))
print(psutil.process_iter())

from pprint import pprint
print('Disk Partition')
pprint(psutil.disk_partitions())
# pprint(psutil.disk_usage())
