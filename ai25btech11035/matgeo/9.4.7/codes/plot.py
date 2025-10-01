import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic function
def quadratic(x):
    return 16*x**2 + 8*x + 1

# Generate x values for the parabola
x_values = np.linspace(-1, 0.5, 400)
y_values = quadratic(x_values)

# Roots of the quadratic equation
roots_x = [0.25, 0.25]
roots_y = [0, 0]

# Plot the parabola
plt.plot(x_values, y_values, label='Parabola: 16x^2 + 8x + 1')

# Mark the roots on the x-axis
plt.scatter(roots_x, roots_y, color='red', label='Roots')

# Plot x-axis line
plt.axhline(0, color='black', linewidth=0.7)

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola and Roots of the Quadratic Equation')

plt.legend()
plt.grid(True)
plt.savefig('../figs/img.png')
plt.show()
