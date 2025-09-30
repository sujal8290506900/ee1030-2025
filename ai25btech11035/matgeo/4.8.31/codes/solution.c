#include <stdio.h>
#include "vectfunc.h"

// Cross product implementation
void cross_product(const double a[3], const double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Dot product implementation
double dot_product(const double a[3], const double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Scale vector
void scale_vector(const double v[3], double k, double result[3]) {
    for (int i=0; i<3; i++) {
        result[i] = k * v[i];
    }
}

// Find d vector as per problem
void find_vector_d(const double a[3], const double b[3], const double c[3], double scalar_cdotd, double d[3]) {
    double cross[3];
    cross_product(a, b, cross);
    double dot = dot_product(c, cross);
    double k = scalar_cdotd / dot;
    scale_vector(cross, k, d);
}

int main() {
    double a[3] = {2, -1, 1};
    double b[3] = {3, 0, -1};
    double c[3] = {2, 1, -2};
    double scalar_cdotd = 3.0;

    double d[3];
    find_vector_d(a, b, c, scalar_cdotd, d);

    printf("Vector d: (%.0lf, %.0lf, %.0lf)\n", d[0], d[1], d[2]);
    return 0;
}
