# logistic distribution is used to describe growth
# used extensively in machine learning in logistic regression, neural networks, etc
# loc   - mean, where the peak is (default 0)
# scale - standard deviation, the flatness of distribution (default 1)
# size  - the shape of the returned array

from numpy import random

x = random.logistic(loc = 1, scale = 2, size = (2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size = 1000), hist=False)
plt.show()