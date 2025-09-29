import math
import sys   

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
import subprocess
import shlex
#end if
# Points as column vectors
A = np.array([1, 3]).reshape(-1, 1)
B = np.array([0, 0]).reshape(-1, 1)
D1 = np.array([2, 0]).reshape(-1, 1)
D2 = np.array([-2, 0]).reshape(-1, 1)

coords = np.block([[A, B, D1, D2]])

# Generate line segments
AB = line_gen(A, B)
BD1 = line_gen(B, D1)
D1A = line_gen(D1, A)
BD2 = line_gen(B, D2)
D2A = line_gen(D2, A)

# Plot lines
plt.plot(AB[0, :], AB[1, :], label='AB')
plt.plot(BD1[0, :], BD1[1, :], label='BD1')
plt.plot(D1A[0, :], D1A[1, :], label='D1A')
plt.plot(BD2[0, :], BD2[1, :], label='BD2')
plt.plot(D2A[0, :], D2A[1, :], label='D2A')

# Plot points
plt.scatter(coords[0, :], coords[1, :], color='red')

# Label points
plt.text(A[0], A[1], "A(1,3)")
plt.text(B[0], B[1], "B(0,0)")
plt.text(D1[0], D1[1], "D1(2,0)")
plt.text(D2[0], D2[1], "D2(-2,0)")

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
plt.savefig('../figs2/img.png')
plt.show()
