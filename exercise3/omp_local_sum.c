#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <math.h>

#define MAX_THREADS 128

void generate_random(double *input, size_t size) {
    for (size_t i = 0; i < size; i++) {
        input[i] = rand() / (double)(RAND_MAX);
    }
}

double omp_local_sum(double *x, size_t size, int num_threads) {
    double local_sum[MAX_THREADS] = {0.0}; 

    #pragma omp parallel num_threads(num_threads)
    {
        int thread_num = omp_get_thread_num();
        double sum = 0.0;

        #pragma omp for
        for (size_t i = 0; i < size; i++) {
            sum += x[i];
        }

        local_sum[thread_num] = sum; 
    }

    double final_sum = 0.0;
    for (int i = 0; i < num_threads; i++) {
        final_sum += local_sum[i];
    }

    return final_sum;
}

int main() {
    const size_t array_size = 10000000; 
    const int num_trials = 10;
    double *array = malloc(array_size * sizeof(double));
    double times[num_trials];
    double total_time = 0.0, avg_time, stddev_time = 0.0;
    int thread_nums[] = {1, 32, 64, 128};
    int num_thread_counts = sizeof(thread_nums) / sizeof(thread_nums[0]);

    generate_random(array, array_size);

    for (int i = 0; i < num_thread_counts; i++) {
        int num_threads = thread_nums[i];
        total_time = 0.0;

        for (int trial = 0; trial < num_trials; trial++) {
            double start_time = omp_get_wtime();
            double sum = omp_local_sum(array, array_size, num_threads);
            double end_time = omp_get_wtime();
            times[trial] = end_time - start_time;
            total_time += times[trial];
        }

        avg_time = total_time / num_trials;

        for (int trial = 0; trial < num_trials; trial++) {
            stddev_time += (times[trial] - avg_time) * (times[trial] - avg_time);
        }
        stddev_time = sqrt(stddev_time / num_trials);

        printf("Threads: %d, Average Time taken: %f seconds, Standard Deviation of Time: %f seconds\n", num_threads, avg_time, stddev_time);
    }

    free(array);
    return 0;
}