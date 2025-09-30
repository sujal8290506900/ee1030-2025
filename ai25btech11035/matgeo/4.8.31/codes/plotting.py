import matplotlib.pyplot as plt
import numpy as np

# Define vectors
A = np.array([2, -1, 1])
B = np.array([3, 0, -1])
C = np.array([2, 1, -2])
D = np.array([3, 15, 9])

origin = np.array([0, 0, 0])  # Origin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to plot a vector with label
def plot_vector(vec, label, color):
    ax.quiver(*origin, *vec, color=color, label=label, length=1, normalize=True)

# Plot each vector
plot_vector(A, 'A', 'r')
plot_vector(B, 'B', 'g')
plot_vector(C, 'C', 'b')
plot_vector(D, 'D', 'm')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title("Vectors A, B, C, and D")
plt.savefig('../figs/img.png')
plt.show()
