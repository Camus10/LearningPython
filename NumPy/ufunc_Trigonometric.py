import numpy as np

x = np.sin(np.pi / 2)
print(x)

arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.sin(arr)
print(x)

# convert into radians
# radians values are pi/180 * degree_values
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# radians to degrees
arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
x = np.rad2deg(arr)
print(x)

# finding angles
# finding angles from values of sine, cos, tan
# sin, cos, tan invers arcsin, arccos, arctan
x = np.arcsin(1.0)
print(x)
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

# hypotenues
# finding hypotenues using pythagoras theorem in numpy
base = 3
perp = 4
x= np.hypot(base, perp)
print(x)