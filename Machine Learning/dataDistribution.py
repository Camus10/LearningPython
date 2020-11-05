import numpy
import matplotlib.pyplot as plt

# create an array containing 250 random floats between 0 and 5
x = numpy.random.uniform(0.0, 5.0, 250)
#print(x)

x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()
# draw histogram with 5 bars
# first bar represents how many values in the array are between 0 and 1
# second bar represents how many values are between 1 and 2

x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()