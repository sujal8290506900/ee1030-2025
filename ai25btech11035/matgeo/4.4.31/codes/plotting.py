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

A = np.array([1,3]).reshape(-1,1)
B = np.array([0,0]).reshape(-1,1)
D_2 = np.array([-2,0]).reshape(-1,1)
D_1 = np.array([2 ,0]).reshape(-1,1)
coords = np.block([[A,B,D_2,D_1]])

AB = line_gen(A,B)
BD_2 = line_gen(B,D_2)
D_2A= line_gen(D_2,A)
BD_1 =line_gen(B,D_1)
D_1A =line_gen(D_1,A)
plt.plot(AB[0,:],AB[1,:])
plt.plot(BD_2[0,:],BD_2[1,:])
plt.plot(D_2A[0,:],D_2A[1,:])
plt.plot(BD_1[0,:],BD_1[1,:])
plt.plot(D_1A[0,:],D_1A[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(1,3)")
plt.text(B[0],B[1],"B(0,0)")
plt.text(D_1[0],D_1[1],"D_1(2,0)")
plt.text(D_2[0],D_2[1],"D_2(-2,0)")
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
