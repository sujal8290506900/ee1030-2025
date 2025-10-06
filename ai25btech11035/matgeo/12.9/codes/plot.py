import numpy as np
import matplotlib.pyplot as plt

# Define the sequences as specified
a = np.array([3, -2])
b = np.array([1, -2])

# Plot sequence a
plt.figure(figsize=(8, 2.5))
plt.stem(np.arange(len(a)), a, basefmt=" ")
plt.title('Sequence a')
plt.xlabel('Index')
plt.ylabel('a[n]')
plt.grid(True)
plt.savefig('../figs/img1.png')
plt.show()

# Plot sequence b in a SEPARATE figure
plt.figure(figsize=(8, 2.5))
plt.stem(np.arange(len(b)), b, basefmt=" ")
plt.title('Sequence b')
plt.xlabel('Index')
plt.ylabel('b[n]')
plt.grid(True)
plt.savefig('../figs/img2.png')
plt.show()

# Compute cross-correlation using the matrix method
La = len(a)
Lb = len(b)
L = La + Lb - 1
cross_corr = np.zeros(L)
k_values = range(-(Lb - 1), La)
for i, k in enumerate(k_values):
    sum_val = 0
    for n in range(La):
        m = n - k
        if 0 <= m < Lb:
            sum_val += a[n] * b[m]
    cross_corr[i] = sum_val

# Plotting the cross-correlation
plt.figure(figsize=(8, 3))
plt.stem(list(k_values), cross_corr, basefmt=" ")
plt.title('Cross-Correlation between sequences a and b')
plt.xlabel('Lag k')
plt.ylabel('Cross-correlation')
plt.grid(True)
plt.show()

# Stem plot for values [-6, 7, -2] at indices [0, 1, 2]
plt.figure(figsize=(8, 3))
plt.stem([0, 1, 2], [-6, 7, -2], basefmt=" ")
plt.title('Stem plot for values -6, 7, -2')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.savefig('../figs/img3.png')
plt.show()
