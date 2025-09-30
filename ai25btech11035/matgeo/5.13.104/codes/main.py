import ctypes

# Load shared library (adjust name/path as per compiled file)
lib = ctypes.CDLL('./libmatgeo13.so')

# Define C structure equivalent in Python
class QuadraticFormParams(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double)]

# Declare argument and return types for C functions for safety
lib.is_positive_definite.argtypes = [ctypes.POINTER(QuadraticFormParams)]
lib.is_positive_definite.restype = ctypes.c_bool

lib.check_condition_b.argtypes = [ctypes.c_double]
lib.check_condition_b.restype = ctypes.c_bool

lib.has_unique_solution.argtypes = [ctypes.POINTER(QuadraticFormParams)]
lib.has_unique_solution.restype = ctypes.c_bool

lib.solve_linear_system.argtypes = [ctypes.POINTER(QuadraticFormParams),
                                   ctypes.POINTER(ctypes.c_double),
                                   ctypes.POINTER(ctypes.c_double)]
lib.solve_linear_system.restype = ctypes.c_bool

# Create instance for parameters: e.g. a=3, b=0.2, c=1.12
params = QuadraticFormParams(3.0, 0.2, 1.12)

# Call functions
print("Is positive definite?", lib.is_positive_definite(ctypes.byref(params)))
print("Check condition |2b| < 1:", lib.check_condition_b(params.b))
print("Has unique solution?", lib.has_unique_solution(ctypes.byref(params)))

# Prepare variables to hold solution
x = ctypes.c_double()
y = ctypes.c_double()
if lib.solve_linear_system(ctypes.byref(params), ctypes.byref(x), ctypes.byref(y)):
    print("Solution x =", x.value, "y =", y.value)
else:
    print("No unique solution found.")
