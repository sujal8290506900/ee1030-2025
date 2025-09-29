import numpy as np
import matplotlib.pyplot as plt

# Points A and B
A = np.array([1, 3])
B = np.array([0, 0])

# Plot line AB
plt.plot([A[0], B[0]], [A[1], B[1]], label='Line AB')

# Plot points A and B
plt.scatter([A[0], B[0]], [A[1], B[1]], color='red')
plt.text(A[0], A[1], 'A(1,3)')
plt.text(B[0], B[1], 'B(0,0)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line joining points A and B')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.savefig('../figs1/img.png')
plt.show()
