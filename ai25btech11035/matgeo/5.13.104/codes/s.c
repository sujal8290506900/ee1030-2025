#include "matgeo13.h"

bool is_positive_definite(const QuadraticFormParams *params) {
    double a = params->a;
    double b = params->b;
    double c = params->c;
    // Check positive definiteness conditions
    return (a > 0.0) && (c > 0.0) && ((a * c - b * b) > 0.0);
}

bool check_condition_b(double b) {
    // check |2b| < 1
    return (2.0 * b > -1.0) && (2.0 * b < 1.0);
}

bool has_unique_solution(const QuadraticFormParams *params) {
    double a = params->a;
    double b = params->b;
    double c = params->c;
    // Matrix determinant should be non-zero
    return (a * c - b * b) != 0.0;
}

bool solve_linear_system(const QuadraticFormParams *params, double *x, double *y) {
    double a = params->a;
    double b = params->b;
    double c = params->c;

    double det = a * c - b * b;
    if(det == 0.0) {
        return false; // No unique solution
    }
    // Using Cramer's rule to solve:
    // ax + by = 1
    // bx + cy = -1
    *x = (c * 1 - b * (-1)) / det;   // (c*1 - b*-1)/det
    *y = (a * (-1) - b * 1) / det;   // (a*-1 - b*1)/det
    return true;
}
