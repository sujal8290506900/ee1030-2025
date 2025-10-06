import ctypes

# Load the shared library
lib = ctypes.CDLL('./libcrosscorr.so')

# Specify argument and return types
lib.cross_correlation.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int)
]
lib.cross_correlation.restype = None

def cross_correlation_py(a, b):
    a_c = (ctypes.c_int * 2)(*a)
    b_c = (ctypes.c_int * 2)(*b)
    out_c = (ctypes.c_int * 3)()
    lib.cross_correlation(a_c, b_c, out_c)
    return list(out_c)

# Example usage
if __name__ == "__main__":
    a = [3, 2]
    b = [1, 2]
    result = cross_correlation_py(a, b)
    print("Cross-correlation result:", result)
