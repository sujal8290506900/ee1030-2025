// quadroots.h
#ifndef QUADROOTS_H
#define QUADROOTS_H

// Struct for 2D vector
typedef struct {
    double x;
    double y;
} Vector2D;

// Struct for 2x2 matrix
typedef struct {
    double a11, a12;
    double a21, a22;
} Matrix2x2;

// Struct to hold quadratic roots (two intersection points)
typedef struct {
    Vector2D root1;
    Vector2D root2;
} QuadRoots;

// Function to compute m^T * V * m where m and V are 2D vector and 2x2 matrix
double mTVm(Vector2D m, Matrix2x2 V);

// Function to compute V * h + u for vectors h, u and matrix V
Vector2D VhPlusU(Matrix2x2 V, Vector2D h, Vector2D u);

// Function to compute scalar m^T * (Vh + u)
double mTVhPlusU(Vector2D m, Vector2D VhPlusU);

// Function to compute scalar gh = h^T V h + 2 u^T h + f
double ghValue(Vector2D h, Matrix2x2 V, Vector2D u, double f);

// Function to find the roots (intersection points) of the quadratic equation
QuadRoots findRoots(Matrix2x2 V, Vector2D u, double f, Vector2D h, Vector2D m);

#endif // QUADROOTS_H
