#ifndef MATRIX_CHECK_H
#define MATRIX_CHECK_H

// Structure to represent the matrix A
typedef struct {
    double alpha;
    double beta;
    double gamma;
} Matrix2x2;

// Function prototype to check if A^2 = 3I condition holds
int check_matrix_condition(Matrix2x2 mat);

#endif
