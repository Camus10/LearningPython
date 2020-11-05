# binomial distribution is a discrete distribution
# n     - number of trials (from 0 to maximum n)
# p     - probability of occurence of each trial (example toss of coin 0.5 each)
# size  - the shape of returned array

from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

# x = random.binomial(n = 10, p = 0.5, size = 10)
# print(x)
sns.distplot(random.binomial(n = 10, p = 0.5, size = 100), hist = True, kde = False)
plt.show()

# difference between normal and binomial distribution
# sns.distplot(random.normal(loc = 50, scale = 5, size = 1000), hist = False, label = 'Normal')
# sns.distplot(random.binomial(n = 100, p = 0.5, size = 1000), hist = False, label = 'Binomial')
# plt.legend(['Normal', 'Binomial'], loc = 'upper left')
# plt.show()