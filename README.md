# C vs. Python Performance Benchmark

For this project, I explored performance benchmarking by comparing how quickly C and Python could find prime numbers. I wrote the same basic program in both languages and measured their execution times to see how much of a difference the programming language made.

I tested numbers up to 10,000, 30,000, 60,000, and 100,000. Each test was run 7 times, and I used the median execution time to account for differences caused by background processes and other factors affecting the CPU.

## Results

I ran the benchmarks on my MacBook Pro with an M5 Max chip.

| Numbers up to | C (ms) | Python (ms) |
| ------------- | ------ | ----------- |
| 10,000 | 0.090 | 2.248 |
| 30,000 | 0.366 | 9.701 |
| 60,000 | 0.909 | 24.797 |
| 100,000 | 1.792 | 50.722 |

C was faster in all four tests, with Python taking approximately 25 to 28 times as long. One thing that I found particularly interesting was how the performance difference increased slightly as the number of values being checked increased. This demonstrated how the difference in execution times between two programming languages can change depending on the workload.

## How to Run It

To run the benchmarks, you will need Python 3 and a C compiler. If you are using a Mac, you can install Apple's Command Line Tools by running:

```bash
xcode-select --install
```

Once everything is installed, open Terminal in the project folder and run:

```bash
python3 run_benchmarks.py
```

The script will automatically run the benchmarks and save the results in `results.csv` and `summary.csv`. It will also create an `environment.txt` file containing information about the computer used to run the tests.

## What I Learned

Through this project, I learned how the way a programming language executes code can significantly affect its performance. Although both programs performed the same task, C was considerably faster than Python across all four tests. I also learned why it is important to run benchmarks multiple times rather than relying on a single result, since execution times can vary depending on other processes running on the computer.

Overall, this experiment helped me better understand how to measure program performance and why factors such as programming language, workload, and testing conditions are important when comparing execution times.

## References

- [Python time documentation](https://docs.python.org/3/library/time.html)
- [Python timeit documentation](https://docs.python.org/3/library/timeit.html)
- [Clang documentation](https://clang.llvm.org/docs/)
