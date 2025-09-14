#include <stdio.h>
#include <stdlib.h>

int main() {
    // Vertices
    int Ax = -4, Ay = -3;
    int Bx = 3, By = -1;
    int Cx = 0, Cy = 5;
    int Dx = -4, Dy =-2;

    // Diagonals as vectors: AC and BD
    int ACx = Cx - Ax; // 0 - (-4) = 4
    int ACy = Cy - Ay; // 5 - (-3) = 8
    int BDx = Dx - Bx; // -4 - 3 = -7
    int BDy = Dy - By; // 2 - (-1) = 3
// Cross product of AC and BD (scalar value)
    int cross = ACx * BDy - ACy * BDx;

    // Area is half the magnitude of the cross product
    double area = 0.5 * abs(cross);

    printf("Area of the quadrilateral by scalar product = %.2lf square units\n", area);

    return 0;
}
    
