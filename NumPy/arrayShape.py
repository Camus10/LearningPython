import numpy as np

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr1.shape)

arr2 = np.array([1, 2, 3, 4], ndmin = 4)
print(arr2)
print('Shape of array : ', arr2.shape)