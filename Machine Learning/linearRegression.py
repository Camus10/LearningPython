# the term of regression is used when you try to find the relationship between variables
# in machine learning and in statistical modeling that relationship is used to predict the outcome of future events

import matplotlib.pyplot as plt 
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
#plt.show()

slope, intercept, r, p, std_err = stats.linregress(x, y)
# slope and intercept values to return a new value
# this new value represents where on the y-axis the corresponding x value will be placed
# r value ranges from 0 (no relationship) to 1 (100% related)
#print(r)

def myfunc(x):
    return slope * x + intercept

# the information have gathered to predict future values
speed = myfunc(10)
print(speed)

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()



