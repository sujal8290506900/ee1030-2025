#include "matrix_check.h"

// Function to check if A^2 = 3I for given matrix A
int check_matrix_condition(Matrix2x2 mat) {
    // The condition from the solution is: 3 = alpha^2 + beta*gamma
    double lhs = mat.alpha * mat.alpha + mat.beta * mat.gamma;
    
    if (lhs == 3.0) {
        return 1; // Condition satisfied
    } else {
        return 0; // Condition not satisfied
    }
}
