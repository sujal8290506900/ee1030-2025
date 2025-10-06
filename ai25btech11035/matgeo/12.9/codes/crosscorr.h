#ifndef CROSSCORR_H
#define CROSSCORR_H

// Inline function to compute cross-correlation of two arrays of length 2
inline void cross_correlation(const int* a, const int* b, int* out) {
    out[0] = a[1] * b[0];                   // Shift +1
    out[1] = a[0] * b[0] + a[1] * b[1];     // Shift 0 (overlap)
    out[2] = a[0] * b[1];                   // Shift -1
}

#endif
