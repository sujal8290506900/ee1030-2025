#include <math.h>
#include "directional_derivative.h"

// Function to calculate the magnitude of a vector
static double vector_magnitude(double x, double y, double z) {
    return sqrt(x*x + y*y + z*z);
}

double directional_derivative(double x, double y, double z, double vx, double vy, double vz) {
    // Compute gradient of F(x,y,z) = x^2 + y^2/4 + z^2/9
    double dFdx = 2 * x;
    double dFdy = y / 2.0;  // derivative with respect to y is y/2 since y^2/4
    double dFdz = (2.0 * z) / 9.0;  // derivative with respect to z is 2z/9 since z^2/9

    // Normalize the direction vector v
    double mag_v = vector_magnitude(vx, vy, vz);
    double ux = vx / mag_v;
    double uy = vy / mag_v;
    double uz = vz / mag_v;

    // Directional derivative = gradient dot unit vector
    double result = dFdx * ux + dFdy * uy + dFdz * uz;
    return result;
}
