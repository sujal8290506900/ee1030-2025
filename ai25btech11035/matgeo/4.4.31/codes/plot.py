import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors
x = np.array([1, 1, 0])
y = np.array([1, 0, 1])
z = np.array([0, 1, 1])
a = np.array([-1, 1, 0])
b = np.array([-1, 0, 1])

vectors = [x, y, z, a, b]
labels = ['x', 'y', 'z', 'a', 'b']
colors = ['r', 'g', 'b', 'm', 'c']

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each vector from origin
for vec, label, color in zip(vectors, labels, colors):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label, arrow_length_ratio=0.1)

# Set axis limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vector Plot')

# Show legend and grid
ax.legend()
ax.grid(True)
plt.savefig('../figs/img.png')
plt.show()
