import ctypes

# Load the shared library (adjust the library name and path accordingly)
lib = ctypes.CDLL('./libeigen_matrix.so')

# Declare the argument and return types for the function
lib.calculate_alpha.argtypes = [ctypes.c_double]
lib.calculate_alpha.restype = ctypes.c_double

# Test the function with eigenvalues
eigenvalues = [1.0, 2.0, 3.0]
for lam in eige\input{beamer/main-slides}nvalues:
    alpha = lib.calculate_alpha(lam)
    print(f"For lambda = {lam}, alpha = {alpha}")
