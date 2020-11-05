# if your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression
# polynomial regression like linear regression uses the relationship between the variables x and y to find the best way to draw a line through the data points

import numpy
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score

# data set example
# registered car's speed and the time of day (hour) the passing occured
# the x-axis represents the hours of the day and the y-axis represents the speed
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
plt.scatter(x, y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# predict the speed of a car passing at 17 pm
speed = mymodel(17)
print(speed)

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# r-squared value ranges from 0 (means no relationship) to 1 (100% related)
print(r2_score(y, mymodel(x)))