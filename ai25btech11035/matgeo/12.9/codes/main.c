#include <stdio.h>
#include "crosscorr.h"

int main() {
    int a[2] = {3, 2};
    int b[2] = {1, 2};
    int out[3];

    cross_correlation(a, b, out);

    printf("Cross-correlation result: %d %d %d\n", out[0], out[1], out[2]);

    return 0;
}
