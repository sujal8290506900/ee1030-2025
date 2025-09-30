import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create meshgrid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Plane 1: 2x - y + 4z = 5  => z = (5 - 2x + y)/4
Z1 = (5 - 2*X + Y) / 4

# Plane 2: 5x - 2.5y + 10z = 6 => z = (6 - 5x + 2.5y)/10
Z2 = (6 - 5*X + 2.5*Y) / 10

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.6, color='lightblue')
ax.plot_surface(X, Y, Z2, alpha=0.6, color='lightgreen')

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title("Planes: 2x - y + 4z = 5 and 5x - 2.5y + 10z = 6")
plt.savefig('../figs/img.png')
plt.show()

