# main.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the shared library
lib = ctypes.CDLL(os.path.abspath("./libmatfun.so"))

# Define Locus struct (same as in matfun.h)
class Locus(ctypes.Structure):
    _fields_ = [
        ("cx", ctypes.c_double),
        ("cy", ctypes.c_double),
        ("r", ctypes.c_double),
        ("is_circle", ctypes.c_int),
        ("m", ctypes.c_double),
        ("c", ctypes.c_double),
    ]

# Set return and argument types
lib.apollonius_locus.restype = Locus
lib.apollonius_locus.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double
]

# Example points
x1, y1 = 0.0, 0.0
x2, y2 = 2.0, 0.0
k = 2.0  # Change to 1.0 for perpendicular bisector

# Call the C function
loc = lib.apollonius_locus(x1, y1, x2, y2, k)

# Plot A and B
plt.scatter([x1, x2], [y1, y2], color='red')
plt.text(x1, y1, "A")
plt.text(x2, y2, "B")

if loc.is_circle:
    theta = np.linspace(0, 2*np.pi, 400)
    x = loc.cx + loc.r * np.cos(theta)
    y = loc.cy + loc.r * np.sin(theta)
    plt.plot(x, y, label=f'Apollonius Circle (k={k})')
    plt.scatter([loc.cx], [loc.cy], color='black', marker='x', label='Center')
else:
    if np.isinf(loc.m):
        x = np.full(100, loc.c)
        y = np.linspace(-5, 5, 100)
    else:
        x = np.linspace(-5, 5, 100)
        y = loc.m * x + loc.c
    plt.plot(x, y, label='Perpendicular Bisector')

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title(f'Apollonius Locus (via C + ctypes) k={k}')
plt.savefig('../figs1/img.png')
plt.show()
