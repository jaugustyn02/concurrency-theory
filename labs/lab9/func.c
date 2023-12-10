#include "math.h"
#include "stdio.h"


double func(double x){
    return sin(x)*x*x;
}

int main(){

    double a = 0.0;
    double b = 1.0;
    int n = 100000000;
    double h = (b-a)/n;
    double sum = 0.0;
    int i;

    #pragma omp parallel for reduction(+:sum)
    for (i = 1; i < n; i++){
        sum += func(a + i*h);
    }
    sum += (func(a) + func(b))/2.0;
    sum *= h;
    printf("The integral is %f\n", sum);

    return 0;
}