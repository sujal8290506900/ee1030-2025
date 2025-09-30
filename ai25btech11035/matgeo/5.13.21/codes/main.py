import ctypes

# Define the Matrix2x2 structure matching the C struct
class Matrix2x2(ctypes.Structure):
    _fields_ = [
        ("m11", ctypes.c_int32),
        ("m12", ctypes.c_int32),
        ("m21", ctypes.c_int32),
        ("m22", ctypes.c_int32),
    ]

# Load the shared library (adjust path if needed)
lib = ctypes.CDLL("./libmatrix_inverse.so")

# Specify argument and return types for compute_inverse function
lib.compute_inverse.argtypes = [ctypes.c_int32, ctypes.POINTER(Matrix2x2)]
lib.compute_inverse.restype = None

# Create an instance of Matrix2x2 to hold result
inverse_matrix = Matrix2x2()

# Call the function with n = 13
lib.compute_inverse(13, ctypes.byref(inverse_matrix))

# Print the result
print("Inverse matrix for n=13:")
print(f"[{inverse_matrix.m11} {inverse_matrix.m12}]")
print(f"[{inverse_matrix.m21} {inverse_matrix.m22}]")
