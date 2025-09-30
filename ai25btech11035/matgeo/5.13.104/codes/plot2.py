import numpy as np
import matplotlib.pyplot as plt

# Coefficients matrix
A = np.array([[6, 6],
              [6, 9]])
# Constants vector
B = np.array([0, 0])

# Check if the system has a unique solution by determinant of A
det = np.linalg.det(A)
print("Determinant of coefficient matrix:", det)

if det == 0:
    print("The lines are either parallel or coincide; no unique intersection.")
    # Plot lines anyway

# Define x range for plotting
x_vals = np.linspace(-10, 10, 400)

# Calculate y values from equations
# From first: 6x + 6y = 0 => y = -x
y1 = -x_vals
# From second: 6x + 9y = 0 => y = -2/3 x
y2 = (-6/9) * x_vals  # simplifies to -2/3 x

# Plot lines
plt.plot(x_vals, y1, label='6x + 6y = 0 (y = -x)')
plt.plot(x_vals, y2, label='6x + 9y = 0 (y = -2/3 x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of two lines')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.savefig('../figs2/img.png')
plt.show()
