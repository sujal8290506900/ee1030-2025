// quadroots.c
#include <stdio.h>
#include <math.h>
#include "quadroots.h"

double mTVm(Vector2D m, Matrix2x2 V) {
    return m.x * (V.a11 * m.x + V.a12 * m.y) + m.y * (V.a21 * m.x + V.a22 * m.y);
}

Vector2D VhPlusU(Matrix2x2 V, Vector2D h, Vector2D u) {
    Vector2D result;
    result.x = V.a11 * h.x + V.a12 * h.y + u.x;
    result.y = V.a21 * h.x + V.a22 * h.y + u.y;
    return result;
}

double mTVhPlusU(Vector2D m, Vector2D vec) {
    return m.x * vec.x + m.y * vec.y;
}

double ghValue(Vector2D h, Matrix2x2 V, Vector2D u, double f) {
    double val = h.x * (V.a11 * h.x + V.a12 * h.y) + h.y * (V.a21 * h.x + V.a22 * h.y);
    val += 2 * (u.x * h.x + u.y * h.y) + f;
    return val;
}

QuadRoots findRoots(Matrix2x2 V, Vector2D u, double f, Vector2D h, Vector2D m) {
    QuadRoots roots;
    double mTvM = mTVm(m, V);
    Vector2D Vh_u = VhPlusU(V, h, u);
    double mTvH_u = mTVhPlusU(m, Vh_u);
    double gh = ghValue(h, V, u, f);

    double discriminant = mTvH_u * mTvH_u - mTvM * gh;
    if (discriminant < 0) {
        // No real roots, setting roots to NaN
        roots.root1.x = roots.root1.y = roots.root2.x = roots.root2.y = NAN;
        return roots;
    }

    double sqrt_disc = sqrt(discriminant);

    // Roots: h + m * t; t = (-mTvH_u ± sqrt_disc) / mTvM
    roots.root1.x = h.x + m.x * ((-mTvH_u + sqrt_disc) / mTvM);
    roots.root1.y = h.y + m.y * ((-mTvH_u + sqrt_disc) / mTvM);

    roots.root2.x = h.x + m.x * ((-mTvH_u - sqrt_disc) / mTvM);
    roots.root2.y = h.y + m.y * ((-mTvH_u - sqrt_disc) / mTvM);

    return roots;
}

#ifdef TESTING
int main() {
    Matrix2x2 V = {16, 0, 0, 0};
    Vector2D u = {4, 0};
    double f = 1;
    Vector2D h = {0, 0};
    Vector2D m = {1, 0};

    QuadRoots roots = findRoots(V, u, f, h, m);
    printf("Roots of quadratic:\n");
    printf("Root1: (%f, %f)\n", roots.root1.x, roots.root1.y);
    printf("Root2: (%f, %f)\n", roots.root2.x, roots.root2.y);
    return 0;
}
#endif
