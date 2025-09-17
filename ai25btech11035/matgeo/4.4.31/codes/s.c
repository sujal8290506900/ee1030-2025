#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    // Coordinates for A, B
    int x1 = 1, y1 = 3;
    int x2 = 0, y2 = 0;

    // Calculate slope and intercept
    float m = (float)(y2 - y1) / (x2 - x1); // Slope
    float c = y1 - m * x1; // Intercept
    printf("Equation of line AB: y = %.2fx + %.2f\n", m, c);

    // Area of triangle formula in coordinates:
    // Area = (1/2) * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
    // Let D(k,0) = (x3, y3)
    int y3 = 0;
    float area_target = 3.0;
    // Substitute:
    // area = 0.5 * |1*(0-0) + 0*(0-3) + k*(3-0)|
    //       = 0.5 * |3*k|
    // Set 0.5 * |3*k| = 3  => |k| = 2
    float k1 = 2.0, k2 = -2.0;

    printf("Possible values of k for D(k,0): %.2f and %.2f\n", k1, k2);

    return 0;
}
