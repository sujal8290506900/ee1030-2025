// main.#include<math.hc
#include <stdio.h>
#include "matfun.h"
#include<math.h>
int main() {
    double x1 = 0, y1 = 0;
    double x2 = 2, y2 = 0;
    double k = 2;  // Try k = 1 for line

    Locus loc = apollonius_locus(x1, y1, x2, y2, k);

    if (loc.is_circle) {
        printf("Apollonius Circle:\n");
        printf("Center: (%.3f, %.3f)\n", loc.cx, loc.cy);
        printf("Radius: %.3f\n", loc.r);
    } else {
        printf("Perpendicular Bisector Line:\n");
        if (isinf(loc.m)) {
            printf("x = %.3f\n", loc.c);
        } else {
            printf("y = %.3fx + %.3f\n", loc.m, loc.c);
        }
    }

    return 0;
}
