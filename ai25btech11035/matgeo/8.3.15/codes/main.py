import ctypes
from ctypes import Structure, c_double, POINTER

# Matching C Point struct
class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# Matching C Triangle struct
class Triangle(Structure):
    _fields_ = [("A", Point), ("B", Point), ("C", Point)]

# Load compiled shared library (triangle.so or triangle.dll)
lib = ctypes.CDLL("./triangle.so")

# Set argtypes and restype for C functions
lib.calculate_equilateral_triangle.argtypes = [c_double, POINTER(Triangle)]
lib.calculate_equilateral_triangle.restype = None

lib.compute_side_length.argtypes = [POINTER(Triangle)]
lib.compute_side_length.restype = c_double

lib.print_triangle.argtypes = [POINTER(Triangle)]
lib.print_triangle.restype = None

# Create Triangle instance
tri = Triangle()

# Parameter 'a' (parabola constant)
a = 1.0

# Calculate triangle points using C function
lib.calculate_equilateral_triangle(a, ctypes.byref(tri))

# Print vertices using C print function
lib.print_triangle(ctypes.byref(tri))

# Compute and print side length
side_length = lib.compute_side_length(ctypes.byref(tri))
print(f"Equilateral triangle side length: {side_length:.4f}")
