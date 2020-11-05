# chi square distribution is used as a basis to verify the hypothesis
# df    - degree of freedom
# size  - the shape of the returned array

from numpy import random

x = random.chisquare(df = 2, size = (2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df = 1, size = 1000), hist = False)
plt.show()