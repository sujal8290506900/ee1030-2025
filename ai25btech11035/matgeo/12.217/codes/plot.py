import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# === Define the surface function ===
def F(x, y, z):
    return x**2 + (y**2)/4 + (z**2)/9

# === Gradient function ===
def grad_F(x, y, z):
    return np.array([2*x, y/2, (2*z)/9])

# === Point P ===
P = np.array([1, 2, 3])

# === Gradient at P ===
gradP = grad_F(*P)

# === Unit vector in direction of P (from origin) ===
u = P / np.linalg.norm(P)

# === Directional derivative ===
DuF = np.dot(gradP, u)
proj_vec = DuF * u  # projection of ∇F on u

# === Print computed values ===
print("Gradient at P:", gradP)
print("Unit vector u:", u)
print("Directional derivative (∇F·u):", DuF)

# === Create the figure ===
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d', facecolor='white')

# === Surface grid ===
x = np.linspace(-3, 3, 60)
y = np.linspace(-6, 6, 60)
x, y = np.meshgrid(x, y)
z = np.sqrt(np.clip(9*(3 - x**2 - (y**2)/4), 0, None))

# === Plot the ellipsoidal surface ===
ax.plot_surface(x, y, z, alpha=0.25, color='skyblue', edgecolor='none')

# === Plot point P ===
ax.scatter(*P, color='crimson', s=80, label='Point P(1,2,3)', depthshade=True)

# === Gradient vector (green) ===
ax.quiver(*P, *gradP, color='limegreen', length=2, normalize=True, arrow_length_ratio=0.2, linewidth=2)
ax.text(*(P + gradP/3), "∇F", color='green', fontsize=12)

# === Unit direction vector u (orange) ===
ax.quiver(0, 0, 0, *u, color='darkorange', length=4, normalize=True, arrow_length_ratio=0.2, linewidth=2)
ax.text(*(u*3.5), "û", color='darkorange', fontsize=12)

# === Projection vector (purple) ===
ax.quiver(*P, *proj_vec, color='purple', length=2, normalize=False, arrow_length_ratio=0.2, linewidth=2)
ax.text(*(P + proj_vec*0.5), "Proj(∇F on û)", color='purple', fontsize=11)

# === Styling the 3D plot ===
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('Directional Derivative Visualization', fontsize=15, fontweight='bold', pad=20)

# Axis limits
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 6)
ax.set_zlim(0, 6)

# Clean aesthetic
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')
plt.savefig('../figs/img.png')
plt.show()
