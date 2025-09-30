#ifndef PLANE_GEOMETRY_H
#define PLANE_GEOMETRY_H

// Structure to represent a plane Ax + By + Cz = D
typedef struct {
    double A;
    double B;
    double C;
    double D;
} Plane;

// Function to check if two planes are parallel
int are_planes_parallel(Plane p1, Plane p2);

// Function to check if a plane passes through given point (x, y, z)
int does_plane_pass_through_point(Plane p, double x, double y, double z);

// Function to get the intersection of a plane with the y-axis (x=0, z=0).
// Returns 1 if intersects and writes y value, else returns 0.
// y_out is output parameter for y coordinate of intersection.
int plane_intersects_y_axis(Plane p, double* y_out);

#endif
