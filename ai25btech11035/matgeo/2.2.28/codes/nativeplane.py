import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

# ------------------------
# Step 1: Define planes
# ------------------------
n1, d1 = sp.Matrix([2, 1, -2]), 5            # 2x + y - 2z = 5
n2, d2 = sp.Matrix([3, -6, -2]), 7           # 3x - 6y - 2z = 7

# ------------------------
# Step 2: Function to plot a plane
# ------------------------
def plot_plane(ax, n, d, color, alpha=0.4):
    xx, yy = np.meshgrid(np.linspace(-5,5,15), np.linspace(-5,5,15))
    zz = (d - n[0]*xx - n[1]*yy) / n[2]
    ax.plot_surface(xx, yy, zz, color=color, alpha=alpha)

# ------------------------
# Step 3: Get points on planes for plotting normals
# ------------------------
x, y, z = sp.symbols('x y z')
plane1_eq = n1[0]*x + n1[1]*y + n1[2]*z - d1
plane2_eq = n2[0]*x + n2[1]*y + n2[2]*z - d2

p1 = sp.solve(plane1_eq.subs({y:0, z:0}), x)
p2 = sp.solve(plane2_eq.subs({y:0, z:0}), x)

a1 = np.array([float(p1[0]), 0, 0]) if p1 else np.zeros(3)
a2 = np.array([float(p2[0]), 0, 0]) if p2 else np.zeros(3)

# ------------------------
# Step 4: Plot planes + normals
# ------------------------
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

n1f, d1f = np.array([float(v) for v in n1]), float(d1)
n2f, d2f = np.array([float(v) for v in n2]), float(d2)

plot_plane(ax, n1f, d1f, "cyan", 0.5)
plot_plane(ax, n2f, d2f, "orange", 0.5)

# Plot normal vectors
ax.quiver(a1[0], a1[1], a1[2], n1f[0], n1f[1], n1f[2],
          length=1, color="blue", linewidth=2, label="Normal to Plane 1")
ax.quiver(a2[0], a2[1], a2[2], n2f[0], n2f[1], n2f[2],
          length=1, color="red", linewidth=2, label="Normal to Plane 2")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Planes and Their Normal Vectors")
ax.legend()
plt.savefig('../figs/img.png')
plt.show()
