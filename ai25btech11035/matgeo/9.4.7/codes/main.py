import ctypes
import math

# Define ctypes equivalent of the structs from the header

class Vector2D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

class Matrix2x2(ctypes.Structure):
    _fields_ = [("a11", ctypes.c_double), ("a12", ctypes.c_double), 
                ("a21", ctypes.c_double), ("a22", ctypes.c_double)]

class QuadRoots(ctypes.Structure):
    _fields_ = [("root1", Vector2D), ("root2", Vector2D)]

# Load the shared library (adjust the path and filename as needed)
lib = ctypes.CDLL("./quadroots.so")

# Define argument and return types for the function findRoots
lib.findRoots.argtypes = [Matrix2x2, Vector2D, ctypes.c_double, Vector2D, Vector2D]
lib.findRoots.restype = QuadRoots

# Prepare inputs
V = Matrix2x2(16.0, 0.0, 0.0, 0.0)
u = Vector2D(4.0, 0.0)
f = 1.0
h = Vector2D(0.0, 0.0)
m = Vector2D(1.0, 0.0)

# Call the C function to get roots
roots = lib.findRoots(V, u, f, h, m)

# Print the results
print(f"Root 1: ({roots.root1.x}, {roots.root1.y})")
print(f"Root 2: ({roots.root2.x}, {roots.root2.y})")

