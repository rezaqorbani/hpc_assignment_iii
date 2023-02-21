#include <stdio.h>
#include <stdlib.h>


void gauss_seidel(float *f, int nrows, int ncols) {
    int i, j;
    float *newf = (float *) malloc(nrows * ncols * sizeof(float));
    
    for (i = 1; i < nrows - 1; i++) {
        for (j = 1; j < ncols - 1; j++) {
            newf[i * ncols + j] = 0.25 * (f[i * ncols + j + 1] + f[i * ncols + j - 1] +
                                           f[(i + 1) * ncols + j] + f[(i - 1) * ncols + j]);
        }
    }
    
    for (i = 1; i < nrows - 1; i++) {
        for (j = 1; j < ncols - 1; j++) {
            f[i * ncols + j] = newf[i * ncols + j];
        }
    }
    
    free(newf);
}