#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static int count_primes(int limit) {
    int count = 0;
    for (int n = 2; n <= limit; n++) {
        int prime = 1;
        for (int d = 2; d * d <= n; d++) {
            if (n % d == 0) { prime = 0; break; }
        }
        if (prime) count++;
    }
    return count;
}

static double now_seconds(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return (double)t.tv_sec + (double)t.tv_nsec / 1e9;
}

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "Usage: %s LIMIT\n", argv[0]); return 1; }
    int limit = atoi(argv[1]);
    double t0 = now_seconds();
    int count = count_primes(limit);
    double elapsed = now_seconds() - t0;
    printf("%d,%.9f\n", count, elapsed);
    return 0;
}
