#include <stdio.h>
#include <math.h>
#include "matfun.h"

#define TOL 1e-9

// Function to check vector equality
int vec_equal(double *u, double *v) {
    for (int i = 0; i < DIM; i++) {
        if (fabs(u[i] - v[i]) > TOL) return 0;
    }
    return 1;
}

int main() {
    // Define vectors from PDF
    double x[DIM] = {1, 1, 0};
    double y[DIM] = {1, 0, 1};
    double z[DIM] = {0, 1, 1};

    double a[DIM], b[DIM], temp[DIM], rhs[DIM];

    // a = y - z
    vec_sub(y, z, temp);
    vec_scale(temp, 1.0, a);

    // b = z - x
    vec_sub(z, x, temp);
    vec_scale(temp, 1.0, b);

    printf("x = [%lf, %lf, %lf]\n", x[0], x[1], x[2]);
    printf("y = [%lf, %lf, %lf]\n", y[0], y[1], y[2]);
    printf("z = [%lf, %lf, %lf]\n", z[0], z[1], z[2]);
    printf("a = [%lf, %lf, %lf]\n", a[0], a[1], a[2]);
    printf("b = [%lf, %lf, %lf]\n", b[0], b[1], b[2]);

    // Option A: b = (b·z)(z-x)
    double dot_bz = vec_dot(b, z);
    vec_sub(z, x, temp);
    vec_scale(temp, dot_bz, rhs);
    printf("Option A: %s\n", vec_equal(b, rhs) ? "TRUE" : "FALSE");

    // Option B: a = (a·y)(y-z)
    double dot_ay = vec_dot(a, y);
    vec_sub(y, z, temp);
    vec_scale(temp, dot_ay, rhs);
    printf("Option B: %s\n", vec_equal(a, rhs) ? "TRUE" : "FALSE");

    // Option C: a·b = -(a·y)(b·z)
    double lhsC = vec_dot(a, b);
    double rhsC = -(vec_dot(a, y) * vec_dot(b, z));
    printf("Option C: %s\n", fabs(lhsC - rhsC) < TOL ? "TRUE" : "FALSE");

    // Option D: a = -(a·y)(z-y)
    vec_sub(z, y, temp);
    vec_scale(temp, -(dot_ay), rhs);
    printf("Option D: %s\n", vec_equal(a, rhs) ? "TRUE" : "FALSE");

    return 0;
}
