import ctypes
from ctypes import c_double

# Load the shared library
lib = ctypes.CDLL('./directional_derivative.so')  # Change .so to .dll on Windows

# Define argument types for the C function
lib.directional_derivative.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# Define return type for the C function
lib.directional_derivative.restype = c_double

# Example usage with point (1, 2, 3) and direction vector (1, 2, 3)
x, y, z = 1.0, 2.0, 3.0
vx, vy, vz = 1.0, 2.0, 3.0

result = lib.directional_derivative(x, y, z, vx, vy, vz)
print(f"Directional derivative at point ({x}, {y}, {z}) in direction ({vx}, {vy}, {vz}) is: {result}")
