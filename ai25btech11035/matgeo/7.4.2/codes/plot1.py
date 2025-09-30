# plot_line_bisector.py
import numpy as np
import matplotlib.pyplot as plt

# Points
x1, y1 = 0, 0
x2, y2 = 2, 0

# Midpoint of AB
mx, my = (x1 + x2) / 2, (y1 + y2) / 2

# AB is horizontal → perpendicular bisector is vertical line x = mx
x_line = np.full(100, mx)
y_line = np.linspace(-5, 5, 100)

# Plot
plt.plot(x_line, y_line, label='Perpendicular Bisector (x = 1)')
plt.scatter([x1, x2], [y1, y2], color='red')
plt.text(x1, y1, "A")
plt.text(x2, y2, "B")

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title('Perpendicular Bisector of AB (k = 1)')
plt.savefig('../figs1/img.png')
plt.show()
