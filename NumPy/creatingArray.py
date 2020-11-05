import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# use tuple to create numpy
arr = np.array((1, 2, 3, 4, 5))
print(arr)

print("\n")

# 0 dimension array
a0 = np.array(42)

# 1 dimension array
a1 = np.array([1, 2, 3, 4, 5])

# 2 dimension array
a2= np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 3 dimension array
a3 = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ], 
        [
            [1, 2, 3], 
            [4, 5, 6]
        ]
    ]
)

print(a0.ndim)
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

a5 = np.array([1, 2, 3, 4], ndmin=5)
print(a5)
print(a5.ndim)