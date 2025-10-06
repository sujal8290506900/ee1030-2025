import numpy as np
import matplotlib.pyplot as plt

# Define parabola y = x^2 + 1
x_vals = np.linspace(-3, 3, 400)
y_parabola = x_vals**2 + 1

# Define line x + y = 3 => y = 3 - x
y_line = 3 - x_vals

# Intersection points from solution
intersections_x = [-2, 1]
intersections_y = [5, 2]

# Plot parabola and line
plt.plot(x_vals, y_parabola, label='Parabola: $y=x^2+1$')
plt.plot(x_vals, y_line, label='Line: $x + y = 3$')

# Plot intersection points
plt.scatter(intersections_x, intersections_y, color='red', zorder=5)

# Annotate intersection points
for (x, y) in zip(intersections_x, intersections_y):
    plt.annotate(f'({x},{y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Titles, labels and legend
plt.title('Parabola and Line with Intersection Points')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.savefig('../figs/img.png')
plt.show()
