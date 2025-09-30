#include "plane_geometry.h"
#include <math.h>

int are_planes_parallel(Plane p1, Plane p2) {
    // Two planes are parallel if their normal vectors are proportional:
    // Check if A1/A2 = B1/B2 = C1/C2 (consider zero division cases)
    
    if (p2.A == 0 || p2.B == 0 || p2.C == 0) {
        // Handle zero divisions carefully
        if (p1.A != 0 && p2.A == 0) return 0;
        if (p1.B != 0 && p2.B == 0) return 0;
        if (p1.C != 0 && p2.C == 0) return 0;
    }

    double rA = (p2.A != 0) ? p1.A / p2.A : 0;
    double rB = (p2.B != 0) ? p1.B / p2.B : 0;
    double rC = (p2.C != 0) ? p1.C / p2.C : 0;
    
    // Use a tolerance for floating comparisons
    double tol = 1e-9;
    if (fabs(rA - rB) < tol && fabs(rB - rC) < tol) {
        return 1; // parallel
    }
    return 0; // not parallel
}

int does_plane_pass_through_point(Plane p, double x, double y, double z) {
    // Check if Ax + By + Cz == D within tolerance
    double val = p.A * x + p.B * y + p.C * z;
    double tol = 1e-9;
    if (fabs(val - p.D) < tol) {
        return 1;
    }
    return 0;
}

int plane_intersects_y_axis(Plane p, double* y_out) {
    // y-axis: x=0, z=0; plug into plane equation: B*y = D
    if (fabs(p.B) < 1e-9) {
        return 0; // no intersection since B=0 means no y solution
    }
    *y_out = p.D / p.B;
    return 1;
}
