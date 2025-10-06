#include <stdio.h>
#include "matgeo_area.h"

int calculate_intersections(Point2D points[2]) {
    // lambda roots from the quadratic equation
    double lambda1 = -2.0;
    double lambda2 = 1.0;

    // Calculate intersection points based on lambda values
    points[0].x = lambda1;
    points[0].y = 3 - lambda1;
    points[1].x = lambda2;
    points[1].y = 3 - lambda2;

    return 2;
}

double calculate_area(double x_start, double x_end) {
    // Integral helper function
    double integral_at(double x) {
        return 2 * x - (x * x) / 2.0 - (x * x * x) / 3.0;
    }

    return integral_at(x_end) - integral_at(x_start);
}

int main() {
    Point2D points[2];
    int count = calculate_intersections(points);
    printf("Intersection points:\n");
    for (int i = 0; i < count; i++) {
        printf("(%lf, %lf)\n", points[i].x, points[i].y);
    }

    double area = calculate_area(points[0].x, points[1].x);
    printf("Area bounded by curves: %lf\n", area);

    return 0;
}
