from numpy import random

x = random.randint(100)
print(x)

# random float from 0 to 1
x = random.rand()
print(x)

# create 1 dimension array cointaining 5 indexs
x = random.randint(100, size = (5))
print(x)

# create 2 dimension array
# 3 rows containing 5 indexs
x = random.randint(100, size = (3, 5))
print(x)

# generate a 1 dimension array containing 5 indexs of float
x = random.rand(5)
print(x)

# generate a 2 dimension arrays of float
# 3 rows containing 5 indexs
x = random.rand(3, 5)
print(x)

x = random.choice([3, 5, 7, 9])
print(x)
x = random.choice([3, 5, 7, 9], size = (3, 5))
print(x)