# poisson distribution is a discrete distribution
# it estimates how many times an event can happen in a specified time
# example : if someone eats rice twice a day what is probability he will eat trice?
# lam - rate or known number of occurences
# size - the shape of the returned array

from numpy import random

x = random.poisson(lam = 2, size = 10)
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(random.poisson(lam = 2, size = 1000), kde = False)
# plt.show()