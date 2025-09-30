#include <stdio.h>
#include <math.h>
#include "triangle.h"

void calculate_equilateral_triangle(double a, Triangle* tri) {
    tri->A.x = 0.0;
    tri->A.y = 0.0;

    tri->B.x = 12 * a;
    tri->B.y = sqrt(48) * a;

    tri->C.x = 12 * a;
    tri->C.y = -sqrt(48) * a;
}

double compute_side_length(const Triangle* tri) {
    // Since A is at origin and B, C are symmetrical on y-axis
    return 2 * tri->B.y; 
}

void print_triangle(const Triangle* tri) {
    printf("Triangle vertices:\n");
    printf("A (%.2f, %.2f)\n", tri->A.x, tri->A.y);
    printf("B (%.2f, %.2f)\n", tri->B.x, tri->B.y);
    printf("C (%.2f, %.2f)\n", tri->C.x, tri->C.y);
}
