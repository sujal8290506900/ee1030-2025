import ctypes

# Load the shared library (adjust the path as needed, e.g., "./linear_eq.so")
lib = ctypes.CDLL("./linear_eq.so")

# Prepare ctypes double variables to receive the results
x = ctypes.c_double()
y = ctypes.c_double()

# Declare the signature of the C function
lib.solve_linear_system.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.solve_linear_system.restype = None

# Call the C function providing addresses of x and y
lib.solve_linear_system(ctypes.byref(x), ctypes.byref(y))

print("Solution from C code:")
print("x =", x.value)
print("y =", y.value)
main