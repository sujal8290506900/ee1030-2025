#ifndef TRIANGLE_H
#define TRIANGLE_H

typedef struct {
    double x;
    double y;
} Point;

typedef struct {
    Point A;
    Point B;
    Point C;
} Triangle;

void calculate_equilateral_triangle(double a, Triangle* tri);
double compute_side_length(const Triangle* tri);
void print_triangle(const Triangle* tri);

#endif // TRIANGLE_H
