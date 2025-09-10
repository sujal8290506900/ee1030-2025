#include <stdio.h>
#include <math.h>

// Function to compute dot product
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to compute magnitude of a vector
double magnitude(double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

int main() {
    // Normal vectors of the two planes
    double n1[3] = {2, 1, -2};   // for plane 2x + y - 2z = 5
    double n2[3] = {3, -6, -2};  // for plane 3x - 6y - 2z = 7

    // Dot product
    double dot_val = dot(n1, n2);

    // Magnitudes
    double mag1 = magnitude(n1);
    double mag2 = magnitude(n2);

    // Cos(theta)
    double cos_theta = dot_val / (mag1 * mag2);

    // Angle in radians and degrees
    double theta_rad = acos(cos_theta);
    double theta_deg = theta_rad * 180.0 / M_PI;

    // Output
    printf("Dot product = %.2f\n", dot_val);
    printf("|n1| = %.2f, |n2| = %.2f\n", mag1, mag2);
    printf("cos(theta) = %.4f\n", cos_theta);
    printf("Angle between planes = %.4f radians = %.2f degrees\n", theta_rad, theta_deg);

    return 0;
}
