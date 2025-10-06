import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors from the screenshots
P = np.array([1, 2, 3])
grad_F = np.array([2, 1, 2/3])

vectors = [P, grad_F]
labels = [r'$\mathbf{P}$', r'$\nabla F(1,2,3)$']
colors = ['b', 'r']

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each vector from origin
for vec, label, color in zip(vectors, labels, colors):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label, arrow_length_ratio=0.1)

# Set axis limits for clarity
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])

# Axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of $\\mathbf{P}$ and $\\nabla F(1,2,3)$')

# Show legend and grid
ax.legend()
ax.grid(True)
plt.savefig('../figs/img.png')
plt.show()
