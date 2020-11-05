# standard deviation is a number that describes how the spread out the values are
# a low standard deviation means that most of the numbers are close to mean (average) value
# a high standard deviation means that the values are spread out over a wider range

import numpy

# example data set
speed1 = [86, 87, 88, 86, 87, 85, 86]
speed2 = [32, 111, 138, 28, 59, 77, 97]

x = numpy.std(speed1)
print(x)
x = numpy.std(speed2)
print(x)
x = numpy.var(speed2)
print(x)