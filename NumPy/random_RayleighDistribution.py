# rayleigh distribution is used in signal processing
# scale - standard deviation decides how flat the distribution will be default
# size  - the shape returned array

from numpy import random

x = random.rayleigh(scale  =2, size = (2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()