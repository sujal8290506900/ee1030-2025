import ctypes
from ctypes import c_double, c_int, POINTER, Structure

# Define Plane struct matching C struct
class Plane(Structure):
    _fields_ = [("A", c_double),
                ("B", c_double),
                ("C", c_double),
                ("D", c_double)]

# Load shared library (assumed named libplane_geometry.so or .dll depending on OS)
lib = ctypes.CDLL("./libplane_geometry.so")

# Define argument and return types
lib.are_planes_parallel.argtypes = (Plane, Plane)
lib.are_planes_parallel.restype = c_int

lib.does_plane_pass_through_point.argtypes = (Plane, c_double, c_double, c_double)
lib.does_plane_pass_through_point.restype = c_int

lib.plane_intersects_y_axis.argtypes = (Plane, POINTER(c_double))
lib.plane_intersects_y_axis.restype = c_int

# Example usage
p1 = Plane(2.0, 1.0, 4.0, 5.0)
p2 = Plane(5.0, 2.5, 10.0, 6.0)

print("Are planes parallel?", bool(lib.are_planes_parallel(p1, p2)))

point = (0.0, 0.0, 54.0)
print("Plane 1 passes through point?", bool(lib.does_plane_pass_through_point(p1, *point)))
print("Plane 2 passes through point?", bool(lib.does_plane_pass_through_point(p2, *point)))

y_val = c_double()
if lib.plane_intersects_y_axis(p1, ctypes.byref(y_val)):
    print("Plane 1 intersects y-axis at y =", y_val.value)
else:
    print("Plane 1 does not intersect y-axis")

if lib.plane_intersects_y_axis(p2, ctypes.byref(y_val)):
    print("Plane 2 intersects y-axis at y =", y_val.value)
else:
    print("Plane 2 does not intersect y-axis")
