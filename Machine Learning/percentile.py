# percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than

import numpy

# example data set
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]


x = numpy.percentile(ages, 75)
print(x)
# means that 75% of people are 43 or younger

# what is the age that 90% of the people are younger than?
x = numpy.percentile(ages, 90)
print(x)