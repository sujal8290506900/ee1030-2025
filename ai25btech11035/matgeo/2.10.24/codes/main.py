import ctypes
import numpy as np

# Load the shared library (assume 'libmatfun1.so' is compiled from matfun-1.h + its .c)
matlib = ctypes.CDLL('./libmatfun1.so')

# Helper: create C array for point
def create_point(x, y):
    arr_type = ctypes.c_double * 2
    arr = arr_type(x, y)
    return arr

# Points
A = create_point(1, 3)
B = create_point(0, 0)
D1 = create_point(2, 0)
D2 = create_point(-2, 0)

# Equation of line
m = (A[1] - B[1]) / (A[0] - B[0])
c = B[1] - m*B[0]
print(f"Equation of line: y = {m:.2f} x + {c:.2f}")

# Vector differences
vecAB = np.array([A[0] - B[0], A[1] - B[1]])
vecD1B = np.array([D1[0] - B[0], D1[1] - B[1]])
vecD2B = np.array([D2[0] - B[0], D2[1] - B[1]])

# Area formula: 0.5 * abs((A-B) x (D-B))
area1 = 0.5 * abs(vecAB[0]*vecD1B[1] - vecAB[1]*vecD1B[0])
area2 = 0.5 * abs(vecAB[0]*vecD2B[1] - vecAB[1]*vecD2B[0])
print(f"For D(2,0), Area ABD = {area1:.2f}")
print(f"For D(-2,0), Area ABD = {area2:.2f}")
