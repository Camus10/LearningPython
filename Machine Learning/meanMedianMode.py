# mean - the average value
# median - the mid point value
# mode the most common value

import numpy
from scipy import stats

# example for data set
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


# the mean value is the average value
x = numpy.mean(speed)
print(x)

# the median value is the value in the middle after you have sorted all the values
x = numpy.median(speed)
print(x)

# the mode value is th evalue that appears the most number of times
x = stats.mode(speed)
print(x) 