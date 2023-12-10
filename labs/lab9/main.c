#include <stdio.h>
#include <omp.h>

int main() {
//    Vector * Scalar
//    int vec[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//    int scalar = 2;
//    #pragma omp parallel shared(vec)
//    {
//        #pragma omp for
//        for (int i = 0; i < 10; i++) {
//            printf("Thread %d: vec[%d] = %d\n", omp_get_thread_num(), i, vec[i]);
//            vec[i] = vec[i] * scalar;
//        }
//    }
//    printf("vec: ");
//    for (int i = 0; i < 10; i++) {
//        printf("%d ", vec[i]);
//    }
//    printf("\n");
//    return 0;

//     Vector * Vector = Scalar
    int const vec1[10] = {1, 2, 3, 4};
    int const vec2[10] = {5, 4, 3, 2};
    int scalar = 0;
    # pragma omp parallel for shared(scalar)
        for (int i = 0; i < 10; i++) {
            scalar += vec1[i] * vec2[i];
        }
    printf("Skalar: %d\n", scalar);
}
