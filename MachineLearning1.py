#
# import numpy
#
#
# speed_car = [32,111,138,28,59,77,97]
# x2 = numpy.mean(speed_car)
#
# print(x2)
# x3 = numpy.std(speed_car)
# print(x3)
#
# x4 = numpy.var(speed_car)
# print(x4)
#
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#
# x5 = numpy.percentile(ages,90)
# print(x5)
#
# x6 = numpy.random.uniform(0.0,5.0, 250)
# print(x6)
#
#

import matplotlib.pyplot
data = (3,4,5,7)
fig, simple_chart = matplotlib.pyplot.subplots()
simple_chart.plot(data)
