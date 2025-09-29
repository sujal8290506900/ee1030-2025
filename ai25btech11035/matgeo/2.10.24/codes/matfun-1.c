#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "matfun-1.h"

int main() {
    // Matrices for points A(1,3), B(0,0)
    double *A = createMat(2,1);
    double *B = createMat(2,1);
    double *D1 = createMat(2,1);
    double *D2 = createMat(2,1);
    A[0] = 1; A[1] = 3;
    B[0] = 0; B[1] = 0;

    // Compute slope m = (y2-y1)/(x2-x1)
    double m = (A[1] - B[1]) / (A[0] - B[0]);
    printf("Equation of line: y = %.2lf x + %.2lf\n", m, B[1] - m * B[0]);

    // Find k for area ABD = 3
    // Area = 0.5 * |(A-B) x (D-B)|
    double area_target = 3.0;
    double k1 = 2.0, k2 = -2.0;
    D1[0] = k1; D1[1] = 0;
    D2[0] = k2; D2[1] = 0;

    // (A-B)
    double vecAB[2] = {A[0]-B[0], A[1]-B[1]};
    // (D1-B)
    double vecD1B[2] = {D1[0]-B[0], D1[1]-B[1]};
    // (D2-B)
    double vecD2B[2] = {D2[0]-B[0], D2[1]-B[1]};
    // Area for D1
    double area1 = 0.5 * fabs(vecAB[0]*vecD1B[1] - vecAB[1]*vecD1B[0]);
    double area2 = 0.5 * fabs(vecAB[0]*vecD2B[1] - vecAB[1]*vecD2B[0]);
    printf("For D(%.2lf,0), Area ABD = %.2lf\n", k1, area1);
    printf("For D(%.2lf,0), Area ABD = %.2lf\n", k2, area2);

    free(A); free(B); free(D1); free(D2);
    return 0;
}
