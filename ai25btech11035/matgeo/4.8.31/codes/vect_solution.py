import ctypes
import numpy as np

# Load the shared library (adjust path as needed)
lib = ctypes.CDLL('./libsolution.so')

# Setup argument and return types
lib.find_vector_d.argtypes = [np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                              np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                              np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                              ctypes.c_double,
                              np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]

lib.find_vector_d.restype = None

# Define vectors a, b, c and scalar
a = np.array([2, -1, 1], dtype=np.double)
b = np.array([3, 0, -1], dtype=np.double)
c = np.array([2, 1, -2], dtype=np.double)
scalar_cdotd = 3.0
d = np.zeros(3, dtype=np.double)

lib.find_vector_d(a, b, c, scalar_cdotd, d)

print(f"Vector d: ({int(d[0])}, {int(d[1])}, {int(d[2])})")
