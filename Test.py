import matplotlib.pyplot

data = (3,6,9,12)
# print(data)

# x = {1:'a'}
# y = x
# print(x is y) 
fig, simple_chart = matplotlib.pyplot.subplots()
simple_chart.plot(data)
matplotlib.pyplot.show()