import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic function
def quadratic(x):
    return 16*x**2 - 8*x + 1

# Generate x values for the parabola plot
x_values = np.linspace(0, 0.5, 400)
y_values = quadratic(x_values)

# Root of the quadratic (double root)
root_x = 0.25
root_y = 0  # quadratic(root_x) is zero

# Plot the parabola curve
plt.plot(x_values, y_values, label='Parabola: 16x^2 - 8x + 1')

# Mark the root(s)
plt.scatter(root_x, root_y, color='red', label='Root at x=0.25')

# Draw x-axis line
plt.axhline(y=0, color='black', linewidth=0.7)

# Labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola and Root of the Quadratic Equation')

# Legend and grid
plt.legend()
plt.grid(True)

# Show plot
plt.savefig('../figs/img.png')
plt.show()
