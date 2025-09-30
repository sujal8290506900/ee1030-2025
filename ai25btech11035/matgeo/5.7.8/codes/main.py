import ctypes
from ctypes import Structure, c_double, c_int

# Define Python representation of the Matrix2x2 struct
class Matrix2x2(Structure):
    _fields_ = [("alpha", c_double),
                ("beta", c_double),
                ("gamma", c_double)]

# Load the compiled shared library (e.g., matrix_check.so or matrix_check.dll)
lib = ctypes.CDLL('./matrix_check.so')  # Adjust path and extension as needed

# Set the argument and return types for the C function
lib.check_matrix_condition.argtypes = [Matrix2x2]
lib.check_matrix_condition.restype = c_int

# Create a sample matrix matching the condition A^2 = 3I (3 = alpha^2 + beta*gamma)
mat = Matrix2x2(alpha=1.0, beta=1.0, gamma=2.0)  # 1^2 + 1*2 = 3

# Call the C function
result = lib.check_matrix_condition(mat)

if result == 1:
    print("Matrix satisfies A^2 = 3I condition.")
else:
    print("Matrix does not satisfy the condition.")
