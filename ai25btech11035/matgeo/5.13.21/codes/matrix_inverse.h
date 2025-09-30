#ifndef MATRIX_INVERSE_H
#define MATRIX_INVERSE_H

#include <stdint.h>

typedef struct {
    int32_t m11, m12;
    int32_t m21, m22;
} Matrix2x2;

void compute_inverse(int32_t n, Matrix2x2* inverse);

#endif // MATRIX_INVERSE_H
