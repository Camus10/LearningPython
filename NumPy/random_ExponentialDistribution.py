# exponential distribution is used for describing time till next event
# example : failure or success
# scale - inverse of rate (see lam in poisson distribution) defaults to 1.0
# size  - the shape of the returned array

from numpy import random

x = random.exponential(scale = 2, size = (2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size = 1000), hist = False)
plt.show()