import numpy as np
import matplotlib.pyplot as plt

# Coefficients matrix
A = np.array([[5, 6],
              [6, 8]])
# Constants vector
B = np.array([1, -1])

# Solve system Ax = B
intersection = np.linalg.solve(A, B)
x_int, y_int = intersection

print(f"Intersection point: x = {x_int}, y = {y_int}")

# x range for plotting
x_vals = np.linspace(x_int - 5, x_int + 5, 400)

# y values for each line
y1 = (1 - 5 * x_vals) / 6
y2 = (-1 - 6 * x_vals) / 8

# Plot lines
plt.plot(x_vals, y1, label='5x + 6y = 1')
plt.plot(x_vals, y2, label='6x + 8y = -1')

# Plot intersection point
plt.plot(x_int, y_int, 'ro', label='Intersection Point')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of two lines with intersection')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.savefig('../figs1/img.png')
plt.show()
