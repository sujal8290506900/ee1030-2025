#ifndef MATGEO13_H
#define MATGEO13_H

#include <stdbool.h>

// Structure to hold the parameters a, b, c
typedef struct {
    double a;
    double b;
    double c;
} QuadraticFormParams;

// Checks if the quadratic form is positive definite (a > 0, c > 0, ac - b^2 > 0)
bool is_positive_definite(const QuadraticFormParams *params);

// Check condition |2b| < 1 for given b
bool check_condition_b(double b);

// Checks if the 2x2 linear system with matrix Q has a unique solution
bool has_unique_solution(const QuadraticFormParams *params);

// Computes the unique solution of system:
// ax + by = 1
// bx + cy = -1
// Returns true if solution exists, solution is placed in x, y
bool solve_linear_system(const QuadraticFormParams *params, double *x, double *y);

#endif // MATGEO13_H
