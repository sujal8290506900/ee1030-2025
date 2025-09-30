#ifndef VECTFUNC_H
#define VECTFUNC_H

// Function declarations

// Cross product of two 3D vectors a and b. Result stored in result.
void cross_product(const double a[3], const double b[3], double result[3]);

// Dot product of two 3D vectors a and b.
double dot_product(const double a[3], const double b[3]);

// Scale vector v by scalar k, store in result.
void scale_vector(const double v[3], double k, double result[3]);

// Solve for vector d perpendicular to a and b such that dot(c, d) = scalar_cdotd.
void find_vector_d(const double a[3], const double b[3], const double c[3], double scalar_cdotd, double d[3]);

#endif
