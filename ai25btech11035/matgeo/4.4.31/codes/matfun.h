#ifndef MATFUN_H
#define MATFUN_H

#define DIM 3

// Basic vector functions
void vec_add(double *a, double *b, double *res);
void vec_sub(double *a, double *b, double *res);
void vec_cross(double *a, double *b, double *res);
double vec_dot(double *a, double *b);
void vec_scale(double *a, double k, double *res);

#endif
