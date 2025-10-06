# example_matfun_usage.py
import ctypes

# Load the shared C library compiled from matfun-1.h and its implementation
lib = ctypes.CDLL('./libmatfun.so')

# Argument and return types
lib.createMat.argtypes = [ctypes.c_int, ctypes.c_int]
lib.createMat.restype = ctypes.POINTER(ctypes.c_double)

lib.printMat.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int]
lib.printMat.restype = None

lib.Matadd.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int]
lib.Matadd.restype = ctypes.POINTER(ctypes.c_double)

# Helper to set matrix values
def set_matrix(arr_ptr, rows, cols, values):
    for i in range(rows):
        for j in range(cols):
            arr_ptr[i * cols + j] = values[i][j]

m, n = 2, 2

# Create matrices using C functions
A = lib.createMat(m, n)
B = lib.createMat(m, n)

# Set matrix values
set_matrix(A, m, n, [[1.0, 2.0], [3.0, 4.0]])
set_matrix(B, m, n, [[5.0, 6.0], [7.0, 8.0]])

print("Matrix A:")
lib.printMat(A, m, n)

print("Matrix B:")
lib.printMat(B, m, n)

# Add matrices
C = lib.Matadd(A, B, m, n)

print("Matrix C = A + B:")
lib.printMat(C, m, n)
