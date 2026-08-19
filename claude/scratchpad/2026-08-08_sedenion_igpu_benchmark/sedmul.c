
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
void sedmul(const float* restrict x, const float* restrict y, float* restrict z, long N) {
#pragma omp parallel for schedule(static)
    for (long g = 0; g < N; ++g) {
        const float x0 = x[0*N + g];
        const float x1 = x[1*N + g];
        const float x2 = x[2*N + g];
        const float x3 = x[3*N + g];
        const float x4 = x[4*N + g];
        const float x5 = x[5*N + g];
        const float x6 = x[6*N + g];
        const float x7 = x[7*N + g];
        const float x8 = x[8*N + g];
        const float x9 = x[9*N + g];
        const float x10 = x[10*N + g];
        const float x11 = x[11*N + g];
        const float x12 = x[12*N + g];
        const float x13 = x[13*N + g];
        const float x14 = x[14*N + g];
        const float x15 = x[15*N + g];
        const float y0 = y[0*N + g];
        const float y1 = y[1*N + g];
        const float y2 = y[2*N + g];
        const float y3 = y[3*N + g];
        const float y4 = y[4*N + g];
        const float y5 = y[5*N + g];
        const float y6 = y[6*N + g];
        const float y7 = y[7*N + g];
        const float y8 = y[8*N + g];
        const float y9 = y[9*N + g];
        const float y10 = y[10*N + g];
        const float y11 = y[11*N + g];
        const float y12 = y[12*N + g];
        const float y13 = y[13*N + g];
        const float y14 = y[14*N + g];
        const float y15 = y[15*N + g];
        z[0*N + g] = x0*y0 - x1*y1 - x2*y2 - x3*y3 - x4*y4 - x5*y5 - x6*y6 - x7*y7 - x8*y8 - x9*y9 - x10*y10 - x11*y11 - x12*y12 - x13*y13 - x14*y14 - x15*y15;
        z[1*N + g] = x0*y1 + x1*y0 + x2*y3 - x3*y2 + x4*y5 - x5*y4 - x6*y7 + x7*y6 + x8*y9 - x9*y8 - x10*y11 + x11*y10 - x12*y13 + x13*y12 + x14*y15 - x15*y14;
        z[2*N + g] = x0*y2 - x1*y3 + x2*y0 + x3*y1 + x4*y6 + x5*y7 - x6*y4 - x7*y5 + x8*y10 + x9*y11 - x10*y8 - x11*y9 - x12*y14 - x13*y15 + x14*y12 + x15*y13;
        z[3*N + g] = x0*y3 + x1*y2 - x2*y1 + x3*y0 + x4*y7 - x5*y6 + x6*y5 - x7*y4 + x8*y11 - x9*y10 + x10*y9 - x11*y8 - x12*y15 + x13*y14 - x14*y13 + x15*y12;
        z[4*N + g] = x0*y4 - x1*y5 - x2*y6 - x3*y7 + x4*y0 + x5*y1 + x6*y2 + x7*y3 + x8*y12 + x9*y13 + x10*y14 + x11*y15 - x12*y8 - x13*y9 - x14*y10 - x15*y11;
        z[5*N + g] = x0*y5 + x1*y4 - x2*y7 + x3*y6 - x4*y1 + x5*y0 - x6*y3 + x7*y2 + x8*y13 - x9*y12 + x10*y15 - x11*y14 + x12*y9 - x13*y8 + x14*y11 - x15*y10;
        z[6*N + g] = x0*y6 + x1*y7 + x2*y4 - x3*y5 - x4*y2 + x5*y3 + x6*y0 - x7*y1 + x8*y14 - x9*y15 - x10*y12 + x11*y13 + x12*y10 - x13*y11 - x14*y8 + x15*y9;
        z[7*N + g] = x0*y7 - x1*y6 + x2*y5 + x3*y4 - x4*y3 - x5*y2 + x6*y1 + x7*y0 + x8*y15 + x9*y14 - x10*y13 - x11*y12 + x12*y11 + x13*y10 - x14*y9 - x15*y8;
        z[8*N + g] = x0*y8 - x1*y9 - x2*y10 - x3*y11 - x4*y12 - x5*y13 - x6*y14 - x7*y15 + x8*y0 + x9*y1 + x10*y2 + x11*y3 + x12*y4 + x13*y5 + x14*y6 + x15*y7;
        z[9*N + g] = x0*y9 + x1*y8 - x2*y11 + x3*y10 - x4*y13 + x5*y12 + x6*y15 - x7*y14 - x8*y1 + x9*y0 - x10*y3 + x11*y2 - x12*y5 + x13*y4 + x14*y7 - x15*y6;
        z[10*N + g] = x0*y10 + x1*y11 + x2*y8 - x3*y9 - x4*y14 - x5*y15 + x6*y12 + x7*y13 - x8*y2 + x9*y3 + x10*y0 - x11*y1 - x12*y6 - x13*y7 + x14*y4 + x15*y5;
        z[11*N + g] = x0*y11 - x1*y10 + x2*y9 + x3*y8 - x4*y15 + x5*y14 - x6*y13 + x7*y12 - x8*y3 - x9*y2 + x10*y1 + x11*y0 - x12*y7 + x13*y6 - x14*y5 + x15*y4;
        z[12*N + g] = x0*y12 + x1*y13 + x2*y14 + x3*y15 + x4*y8 - x5*y9 - x6*y10 - x7*y11 - x8*y4 + x9*y5 + x10*y6 + x11*y7 + x12*y0 - x13*y1 - x14*y2 - x15*y3;
        z[13*N + g] = x0*y13 - x1*y12 + x2*y15 - x3*y14 + x4*y9 + x5*y8 + x6*y11 - x7*y10 - x8*y5 - x9*y4 + x10*y7 - x11*y6 + x12*y1 + x13*y0 + x14*y3 - x15*y2;
        z[14*N + g] = x0*y14 - x1*y15 - x2*y12 + x3*y13 + x4*y10 - x5*y11 + x6*y8 + x7*y9 - x8*y6 - x9*y7 - x10*y4 + x11*y5 + x12*y2 - x13*y3 + x14*y0 + x15*y1;
        z[15*N + g] = x0*y15 + x1*y14 - x2*y13 - x3*y12 + x4*y11 + x5*y10 - x6*y9 + x7*y8 - x8*y7 + x9*y6 - x10*y5 - x11*y4 + x12*y3 + x13*y2 - x14*y1 + x15*y0;
    }
}
int main(int argc,char**argv){
    long N = 1L<<20; int nt = atoi(argv[1]); omp_set_num_threads(nt);
    float *x=aligned_alloc(64,16*N*4),*y=aligned_alloc(64,16*N*4),*z=aligned_alloc(64,16*N*4);
    for(long i=0;i<16*N;i++){x[i]=(float)rand()/RAND_MAX;y[i]=(float)rand()/RAND_MAX;}
    sedmul(x,y,z,N);
    double best=1e9;
    for(int r=0;r<5;r++){
        struct timespec a,b; clock_gettime(CLOCK_MONOTONIC,&a);
        sedmul(x,y,z,N);
        clock_gettime(CLOCK_MONOTONIC,&b);
        double t=(b.tv_sec-a.tv_sec)+(b.tv_nsec-a.tv_nsec)/1e9; if(t<best)best=t;
    }
    printf("threads=%d  %7.2f ms  %6.2f GFLOP/s  %6.2f GB/s eff\n",
           nt, best*1e3, 512.0*N/best/1e9, 3.0*16*N*4/best/1e9);
    return 0;
}
