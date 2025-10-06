import ctypes
from ctypes import Structure, c_double, POINTER, c_int

# Define Point2D struct to match C struct
class Point2D(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# Load the compiled shared library (compile matgeo_area.c as shared library)
lib = ctypes.CDLL('./libmatgeo.so')

# Define argument and result types for C functions
lib.calculate_intersections.argtypes = (POINTER(Point2D),)
lib.calculate_intersections.restype = c_int
lib.calculate_area.argtypes = (c_double, c_double)
lib.calculate_area.restype = c_double

# Allocate array for intersections
points = (Point2D * 2)()

# Call intersection calculation
count = lib.calculate_intersections(points)

print("Intersection Points:")
for i in range(count):
    print(f"({points[i].x}, {points[i].y})")

# Calculate area between intersection x values
area = lib.calculate_area(points[0].x, points[1].x)
print(f"Area bounded by curves: {area}")
