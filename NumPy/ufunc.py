# universal function
# to implement vectorisation in numpy which is way faster than iterating over elements
# provide broadcasting and additional methods like reduce, accumulate, etc that are very helpful for computation
# where - boolean array or condition definig where the operations should take place
# dtype - defining the return type of elements
# out   - output array where the return value should be copied
# vectorisation is converting iterative statements into a vector based operatino is called vectorisation

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
    z.append(i + j)
print(z)

# produce same result
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)