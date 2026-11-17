import csv
import platform
import statistics
import subprocess
import sys
from pathlib import Path

folder = Path(__file__).resolve().parent
limits = [10000, 30000, 60000, 100000]
expected = {10000: 1229, 30000: 3245, 60000: 6057, 100000: 9592}
trials = 7

sdk = subprocess.check_output(
    ["xcrun", "--sdk", "macosx", "--show-sdk-path"], text=True
).strip()

print("Building the C program...")
subprocess.run(
    ["xcrun", "--sdk", "macosx", "clang", "-isysroot", sdk,
     "-O2", "-std=c11", "-D_POSIX_C_SOURCE=199309L", "-Wall", "-Wextra",
     "prime_benchmark.c", "-o", "prime_c"],
    cwd=folder, check=True
)

results = []
summary = []

for limit in limits:
    print(f"Checking numbers up to {limit:,}: running each program 7 times...")
    times = {"C": [], "Python": []}

    for trial in range(1, trials + 1):
        programs = {
            "C": [str(folder / "prime_c"), str(limit)],
            "Python": [sys.executable, str(folder / "prime_benchmark.py"), str(limit)]
        }

        for language, command in programs.items():
            output = subprocess.check_output(command, cwd=folder, text=True).strip()
            prime_count, seconds = output.split(",")
            if int(prime_count) != expected[limit]:
                raise ValueError(f"The {language} program gave the wrong answer for {limit:,}.")

            seconds = float(seconds)
            times[language].append(seconds)
            results.append([limit, trial, language, int(prime_count), seconds])

    c_ms = statistics.median(times["C"]) * 1000
    python_ms = statistics.median(times["Python"]) * 1000
    summary.append([limit, expected[limit], c_ms, python_ms, python_ms / c_ms])

with (folder / "results.csv").open("w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["limit", "trial", "language", "primes_found", "seconds"])
    writer.writerows(results)

with (folder / "summary.csv").open("w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["limit", "primes_found", "c_median_ms", "python_median_ms", "python_over_c_ratio"])
    writer.writerows(summary)

chip = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], text=True).strip()
compiler = subprocess.check_output(["xcrun", "clang", "--version"], text=True).splitlines()[0]
(folder / "environment.txt").write_text(
    f"macOS: {platform.mac_ver()[0]}\n"
    f"Chip: {chip}\n"
    f"Python: {platform.python_version()}\n"
    f"C compiler: {compiler}\n"
    "C optimization: -O2\n"
    "Runs: 7 per language per input size\n"
)

print("\nResults (median time from 7 runs, in milliseconds)")
print(f"{'Numbers up to':>13} {'C (ms)':>11} {'Python (ms)':>13} {'Python took':>18}")
for limit, count, c_ms, python_ms, ratio in summary:
    print(f"{limit:>13,} {c_ms:>11.3f} {python_ms:>13.3f} {ratio:>12.2f}x as long")

print("\nBoth programs found the right number of primes.")
print("Saved the timings in results.csv and summary.csv.")
print("Saved the computer details in environment.txt.")
