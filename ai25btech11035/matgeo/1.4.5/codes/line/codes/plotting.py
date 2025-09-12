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

A = np.array([2,2]).reshape(-1,1)
P = np.array([0,0]).reshape(-1,1)
D = np.array([-1,-1]).reshape(-1,1)
coords = np.block([[A,P,D]])

AP = line_gen(A,P)
PD = line_gen(P,D)

plt.plot(AP[0,:],AP[1,:])
plt.plot(PD[0,:],PD[1,:])

plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(2,2)")
plt.text(P[0],P[1],"P(0,0)")
plt.text(D[0],D[1],"D(-1,-1)")

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')