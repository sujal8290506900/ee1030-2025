import numpy as np
import matplotlib.pyplot as plt
import math

# Parameter a in parabola y^2 = 4ax
a = 1.0

# Vertex A at origin (0,0)
A = (0, 0)

# B and C coordinates
B = (12 * a, math.sqrt(48) * a)
C = (12 * a, -math.sqrt(48) * a)

# Parabola definition for x >= 0
x = np.linspace(0, 15, 500)
y_pos = np.sqrt(4 * a * x)
y_neg = -y_pos

plt.figure(figsize=(10, 8))

# Plot parabola
plt.plot(x, y_pos, 'r-', label='Parabola: $y^2=4ax$')
plt.plot(x, y_neg, 'r-')

# Plot triangle vertices
plt.scatter(*A, color='blue', s=100, zorder=5)
plt.scatter(*B, color='blue', s=100, zorder=5)
plt.scatter(*C, color='blue', s=100, zorder=5)

# Draw triangle edges
triangle_x = [A[0], B[0], C[0], A[0]]
triangle_y = [A[1], B[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, color='green', linewidth=2, label='Equilateral Triangle')

# Label points
plt.text(A[0], A[1] - 0.5, 'A (0,0)', fontsize=12, ha='center')
plt.text(B[0], B[1] + 0.5, f'B ({B[0]:.1f},{B[1]:.1f})', fontsize=12, ha='center')
plt.text(C[0], C[1] - 1, f'C ({C[0]:.1f},{C[1]:.1f})', fontsize=12, ha='center')

plt.title('Parabola with Equilateral Triangle Inscribed')
plt.xlabel('x')
plt.ylabel('y')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.grid(True)
plt.legend()
plt.axis('equal')
plt.savefig('../figs/img.png')
plt.show()
