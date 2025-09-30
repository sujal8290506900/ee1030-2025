# plot_apollonius_circle.py
import numpy as np
import matplotlib.pyplot as plt

# Points
x1, y1 = 0, 0
x2, y2 = 2, 0
k = 2  # any value not equal to 1

# Compute Apollonius circle center and radius
k2 = k * k
cx = (x1 - k2 * x2) / (1 - k2)
cy = (y1 - k2 * y2) / (1 - k2)
d = np.hypot(x1 - x2, y1 - y2)
r = (k * d) / abs(1 - k2)

# Generate circle points
theta = np.linspace(0, 2*np.pi, 400)
x_circle = cx + r * np.cos(theta)
y_circle = cy + r * np.sin(theta)

# Plot
plt.plot(x_circle, y_circle, label=f'Apollonius Circle (k={k})')
plt.scatter([x1, x2], [y1, y2], color='red')
plt.scatter([cx], [cy], color='black', marker='x', label='Center')
plt.text(x1, y1, "A")
plt.text(x2, y2, "B")

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title(f'Apollonius Circle for k = {k}')
plt.savefig('../figs2/img.png')
plt.show()
