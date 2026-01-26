# timing.py

"""
Times how long a snippet of code takes to run
over multiple iterations

"""

import argparse
from collections import namedtuple
from time import perf_counter

Timing = namedtuple("Timing", "repeats elapsed average")


def timeit(code, repeats=10):
    code = compile(code, filename="<string>", mode="exec")
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    stop = perf_counter()
    elapsed = stop - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)


if __name__ == "__main__":
    # get code from argumwents and repeats
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code", type=str, help="The Python code snippet to time.")
    parser.add_argument(
        "-r", "--repeats", type=int, default=10, help="Number of times to repeat the test."
    )
    args = parser.parse_args()
    print(f"timing.. {args.code}...")
    print(timeit(code=str(args.code), repeats=args.repeats))
