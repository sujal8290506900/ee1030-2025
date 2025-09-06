#include <stdio.h>

int main() {
    // Coordinates of A and D
    float Ax = 2.0, Ay = 2.0;
    float Dx = -1.0, Dy = -1.0;

    // Ratio AP:PD = 2:1
    float m = 2.0, n = 1.0;

    // Section formula: P = (m*D + n*A)/(m+n)
    float Px = (m*Dx + n*Ax) / (m + n);
    float Py = (m*Dy + n*Ay) / (m + n);

    printf("The coordinates of point P are: (%.2f, %.2f)\n", Px, Py);
    return 0;
}