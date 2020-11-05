import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.copy()
arr1[0] = 42
print(arr1)
print(x)

arr2 = np.array([1, 2, 3, 4, 5])
y = arr2.view()
arr2[0] = 31
print(arr2)
print(y)

print(x.base)
print(y.base)