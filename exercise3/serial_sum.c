#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <math.h>

double serial_sum(double *x, size_t size)
{
  double sum_val = 0.0;

  for (size_t i = 0; i < size; i++) {
    sum_val += x[i];
  }

  return sum_val;
}

void generate_random(double *input, size_t size)
{
  for (size_t i = 0; i < size; i++) {
    input[i] = rand() / (double)(RAND_MAX);
  }
}

int main() {
    const size_t array_size = 10000000;
    const int num_trials = 10;
    double *array = malloc(array_size * sizeof(double));
    double times[num_trials];
    double total_time = 0.0, avg_time, stddev_time = 0.0;

    generate_random(array, array_size);

    for (int trial = 0; trial < num_trials; trial++) {
        double start_time = omp_get_wtime();
        double sum = serial_sum(array, array_size);
        double end_time = omp_get_wtime();
        times[trial] = end_time - start_time;
        total_time += times[trial];
    }

    avg_time = total_time / num_trials;

    for (int trial = 0; trial < num_trials; trial++) {
        stddev_time += (times[trial] - avg_time) * (times[trial] - avg_time);
    }
    stddev_time = sqrt(stddev_time / num_trials);

    printf("Average Time taken: %f seconds\n", avg_time);
    printf("Standard Deviation of Time: %f seconds\n", stddev_time);

    free(array);
    return 0;
}