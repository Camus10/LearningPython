# to get normal data distribution use random.normal()
# example : iq scores, heartbeat, etc
# loc - (mean) where the peak of bell exists
# scale - (standard deviation) how flat the graph distribution should be
# size - the shape of the returned array

from numpy import random
x = random.normal(size = (2, 3))
print(x)

x = random.normal(loc = 1, scale = 2, size = (2, 3))
print(x)

# visualisation normal distribution
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

# sns.distplot(random.normal(size = 1000), hist = False)
# plt.show()