# distributing following pareto's law
# example : 80 - 20 distribution (20% factors cause 80% outcome)
# a     - shape parameter
# size  - the shape of returned array

from numpy import random

x = random.pareto(a = 2, size = (2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=100), kde=False)
plt.show()