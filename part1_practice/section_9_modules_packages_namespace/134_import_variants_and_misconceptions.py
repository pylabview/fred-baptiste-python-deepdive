import sys
from collections import namedtuple
from time import perf_counter

for key in sorted(sys.modules.keys()):
    print(key)

# Checking in cmath is in sys.modules and/or globals
print(f"Is cmath in sys.modules: {'cmath' in sys.modules}")
print(f"or cmath is in globals : {'cmath' in globals()}")
print("--------------------------------------------")
# Checking in cmath is in sys.modules and/or globals
from cmath import exp

exp(2 + 2j)
print(f"After import cmath and exp, Is cmath in sys.modules: {'cmath' in sys.modules}")
print(f"or cmath is in globals : {'cmath' in globals()}, but is exp? {'exp' in globals()}")
# cmath is not in globals, can't do cmath.sqtr()
# but can be add it
cmath = sys.modules["cmath"]
print("------------------------")
print(f"After 'cmath = sys.modules['cmath']' cmath is in globals : {'cmath' in globals()}")
# Now we can do, and we import all module content into the namespace
cmath.exp(2 + 2j)

Timings = namedtuple("Timings", "timing_1 timing_2 abs_diff rel_diff_perc")


def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1) / timing1 * 100
    timings = Timings(
        round(timing1, 1), round(timing2, 1), round(timing2 - timing1, 1), round(rel_diff, 2)
    )

    return timings


import math

test_reps = 10_000_000

start = perf_counter()
for _i in range(test_reps):
    math.sqrt(2)

end = perf_counter()
elapsed_fully_qualified = end - start
print(f"Elapsed: {elapsed_fully_qualified}")
