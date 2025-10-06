#include <stdio.h>
#include "eigen_matrix.h"

int main() {
    double eigenvalues[] = {1.0, 2.0, 3.0};
    int n = 3;

    for (int i = 0; i < n; i++) {
        double alpha = calculate_alpha(eigenvalues[i]);
        printf("For lambda = %.1f, alpha = %.1f\n", eigenvalues[i], alpha);
    }

    return 0;
}
