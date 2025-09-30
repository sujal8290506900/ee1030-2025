import numpy as np
import matplotlib.pyplot as plt

# Define x range for plotting
x = np.linspace(0, 10, 400)

# Define y from equations:
# y = (6 - x)/2 for x + 2y = 6
# y = (12 - 2*x)/5 for 2x + 5y = 12
y1 = (6 - x) / 2
y2 = (12 - 2*x) / 5

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='x + 2y = 6')
plt.plot(x, y2, label='2x + 5y = 12')

# Plot the intersection point (6, 0)
plt.plot(6, 0, 'ro', label='Solution (6,0)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of system of linear equations')
plt.legend()
plt.grid(True)
plt.ylim(-1, 4)
plt.show()
