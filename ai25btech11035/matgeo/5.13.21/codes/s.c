// s-1.c
#include <stddef.h>
#include <stdint.h>
#include "matrix_inverse.h"

// Function to compute the inverse matrix of A = [[1, n], [0, 1]]
// The inverse = [[1, -n], [0, 1]]
void compute_inverse(int32_t n, Matrix2x2* inverse) {
    if (inverse == NULL)
        return;

    inverse->m11 = 1;
    inverse->m12 = -n;
    inverse->m21 = 0;
    inverse->m22 = 1;
}
