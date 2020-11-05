# a discrete difference means substracting two successive elements

import numpy as np 

# 10 - 10
# 15 - 10
# 25 - 15
# 5 - 25
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)

# performs once again as long as n repetitions
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n = 2)
print(newarr)