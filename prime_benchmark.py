import sys
import time


def count_primes(limit):
    count = 0
    for n in range(2, limit + 1):
        prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                prime = False
                break
            d += 1
        if prime:
            count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 prime_benchmark.py LIMIT")
    limit = int(sys.argv[1])
    start = time.perf_counter()
    result = count_primes(limit)
    elapsed = time.perf_counter() - start
    print(f"{result},{elapsed:.9f}")
