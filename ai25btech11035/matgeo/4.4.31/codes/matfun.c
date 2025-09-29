#include "matfun.h"

// Vector addition
void vec_add(double *a, double *b, double *res) {
    for (int i = 0; i < DIM; i++)
        res[i] = a[i] + b[i];
}

// Vector subtraction
void vec_sub(double *a, double *b, double *res) {
    for (int i = 0; i < DIM; i++)
        res[i] = a[i] - b[i];
}

// Cross product
void vec_cross(double *a, double *b, double *res) {
    res[0] = a[1]*b[2] - a[2]*b[1];
    res[1] = a[2]*b[0] - a[0]*b[2];
    res[2] = a[0]*b[1] - a[1]*b[0];
}

// Dot product
double vec_dot(double *a, double *b) {
    double sum = 0.0;
    for (int i = 0; i < DIM; i++)
        sum += a[i] * b[i];
    return sum;
}

// Scalar multiplication
void vec_scale(double *a, double k, double *res) {
    for (int i = 0; i < DIM; i++)
        res[i] = k * a[i];
}
