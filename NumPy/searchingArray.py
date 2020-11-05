import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.array(arr == 4)
print(x)
x = np.where(arr == 4)
print(x)
x = np.where(arr%2 == 0)
print(x)
x = np.where(arr%2 == 1)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
x = np.searchsorted(arr, 7, side='right')
print(x)

# find the indexes where the values 2, 4, 6 should be inserted
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
# the return value is an array [1, 2, 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order
print(x)
print(arr)