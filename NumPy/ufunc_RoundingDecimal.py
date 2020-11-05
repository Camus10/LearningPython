# there are primarily five ways of rounding off decimals in numpy
# truncation
# fix
# rounding
# floor
# ceil

import numpy as np

# truncation
# remove the decimals and return the float number closest to zero
# trunc() or fix()
arr = np.trunc([-3.16666, 3.6667])
print(arr)
arr = np.fix([-3.16666, 3.6667])
print(arr)

# rounding
# the around() function increments preceding digit or decimal by 1 if >= 5 else do nothing
arr = np.around(3.1666, 2)
print(arr)

# floor
# the floor() function rounds off decimal to nearest lower integer
arr = np.floor([-3.1666, 3.6667])
print(arr)

# ceil
# the ceil() function round off decimal to nearest upper integer
arr = np.ceil([-3.1666, 3.6667])
print(arr)