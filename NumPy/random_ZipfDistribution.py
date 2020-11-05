# zipf distribution are used to sample data based on zipf's law
# zipf's law : in a collection the n-th commmon term is 1/n times of the most common term
# example : 5th common word in english has occurs nearly 1/5th times as of the most used word
# a     - distribution parameter
# size  - the shape of returned array

from numpy import random

x = random.zipf(a = 2, size = (2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a = 2, size = 1000)
sns.distplot(x[x < 10], kde = False)
plt.show()