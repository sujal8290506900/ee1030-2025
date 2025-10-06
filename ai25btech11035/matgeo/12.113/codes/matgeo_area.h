#ifndef MATGEO_AREA_H
#define MATGEO_AREA_H

#ifdef __cplusplus
extern "C" {
#endif

// Struct for 2D points
typedef struct {
    double x;
    double y;
} Point2D;

// Calculate intersections of parabola and line, fills points array with two intersections
int calculate_intersections(Point2D points[2]);

// Calculate area between parabola and line between x_start and x_end
double calculate_area(double x_start, double x_end);

#ifdef __cplusplus
}
#endif

#endif // MATGEO_AREA_H
