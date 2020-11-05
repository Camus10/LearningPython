import numpy as np

# numpy provides the ufunc sinh(), cosh(), tanh() that take values in radians and produce the corresponding sinh, cosh, tanh values

x = np.sinh(np.pi / 2)
print(x)

arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.cosh(arr)
print(x)

# finding angles from values of hyperbolic sine, cos, tan
# example : sinh, cosh, tanh inverse (arcsinh, arccosh, arctanh)

x = np.arcsinh(1.0)
print(x)

arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)