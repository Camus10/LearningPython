import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)
newarr = np.sum([arr1, arr2])
print(newarr)
# axis will sum the numbers in each array
newarr = np.sum([arr1, arr2], axis = 1)
print(newarr)
# calculate partially
# 1
# 1 + 2
# 1 + 2 + 3
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)