import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Load the shared library
lib = ctypes.CDLL(os.path.abspath("./libmatfun.so"))

# Define argument & return types for functions
lib.vec_add.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]

lib.vec_sub.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]

lib.vec_cross.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]

lib.vec_dot.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]
lib.vec_dot.restype = ctypes.c_double

lib.vec_scale.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.c_double,
                          ctypes.POINTER(ctypes.c_double)]

# Helper: Convert numpy vector to ctypes
def to_c_array(vec):
    return (ctypes.c_double * 3)(*vec)

def from_c_array(c_arr):
    return np.array([c_arr[0], c_arr[1], c_arr[2]])

# Define base vectors
x = np.array([1, 1, 0], dtype=np.float64)
y = np.array([1, 0, 1], dtype=np.float64)
z = np.array([0, 1, 1], dtype=np.float64)
a = np.array([-1, 1, 0], dtype=np.float64)
b = np.array([-1, 0, 1], dtype=np.float64)

vectors = [x, y, z, a, b]
labels = ['x', 'y', 'z', 'a', 'b']
colors = ['r', 'g', 'b', 'm', 'c']

# Example: use C cross product between x and y
res_c = (ctypes.c_double * 3)()
lib.vec_cross(to_c_array(x), to_c_array(y), res_c)
cross_xy = from_c_array(res_c)
print("x × y =", cross_xy)

# Plot vectors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for vec, label, color in zip(vectors, labels, colors):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label, arrow_length_ratio=0.1)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('3D Vectors (ctypes + C functions)')
ax.grid(True)

plt.show()
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Load the shared library
lib = ctypes.CDLL(os.path.abspath("./libmatfun.so"))

# Define argument & return types for functions
lib.vec_add.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]

lib.vec_sub.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]

lib.vec_cross.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]

lib.vec_dot.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]
lib.vec_dot.restype = ctypes.c_double

lib.vec_scale.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.c_double,
                          ctypes.POINTER(ctypes.c_double)]

# Helper: Convert numpy vector to ctypes
def to_c_array(vec):
    return (ctypes.c_double * 3)(*vec)

def from_c_array(c_arr):
    return np.array([c_arr[0], c_arr[1], c_arr[2]])

# Define base vectors
x = np.array([1, 1, 0], dtype=np.float64)
y = np.array([1, 0, 1], dtype=np.float64)
z = np.array([0, 1, 1], dtype=np.float64)
a = np.array([-1, 1, 0], dtype=np.float64)
b = np.array([-1, 0, 1], dtype=np.float64)

vectors = [x, y, z, a, b]
labels = ['x', 'y', 'z', 'a', 'b']
colors = ['r', 'g', 'b', 'm', 'c']

# Example: use C cross product between x and y
res_c = (ctypes.c_double * 3)()
lib.vec_cross(to_c_array(x), to_c_array(y), res_c)
cross_xy = from_c_array(res_c)
print("x × y =", cross_xy)

# Plot vectors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for vec, label, color in zip(vectors, labels, colors):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label, arrow_length_ratio=0.1)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('3D Vectors (ctypes + C functions)')
ax.grid(True)

plt.show()
