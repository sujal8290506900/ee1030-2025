// matfun.h
#ifndef MATFUN_H
#define MATFUN_H

// Struct for Circle
typedef struct {
    double cx;
    double cy;
    double r;
    int is_circle; // 1 = circle, 0 = line
    double m; // slope of line (if line)
    double c; // intercept of line (if line)
} Locus;

// Function to compute Apollonius locus
Locus apollonius_locus(double x1, double y1, double x2, double y2, double k);

#endif
