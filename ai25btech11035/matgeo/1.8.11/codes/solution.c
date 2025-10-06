// example_matfun_usage.c
#include <stdio.h>
#include <stdlib.h>
#include "matfun-1.h"

int main() {
    int m = 2, n = 2;

    // Create two 2x2 matrices
    double *A = createMat(m, n);
    double *B = createMat(m, n);

    // Initialize matrix A
    A[0] = 1.0; A[1] = 2.0;
    A[2] = 3.0; A[3] = 4.0;

    // Initialize matrix B
    B[0] = 5.0; B[1] = 6.0;
    B[2] = 7.0; B[3] = 8.0;

    printf("Matrix A:\n");
    printMat(A, m, n);

    printf("Matrix B:\n");
    printMat(B, m, n);

    // Add matrices A and B
    double *C = Matadd(A, B, m, n);

    printf("Matrix C = A + B:\n");
    printMat(C, m, n);

    // Since createMat likely uses malloc, free allocated memory
    free(A);
    free(B);
    free(C);

    return 0;
}
