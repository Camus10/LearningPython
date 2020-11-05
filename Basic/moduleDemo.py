import moduleMine

moduleMine.greeting("Camus")

a = moduleMine.person1["age"]
print(a)

# renaming module
import moduleMine as mx
b = mx.person1["age"]
print(b)

# built-in module
import platform
c = platform.system()
print(c)

# import platform
# x = dir(platform)
# print(x)

# import from module
from moduleMine import person1
print(person1["country"])