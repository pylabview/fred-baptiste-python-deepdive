# 104_decoratores.py
import inspect
from functools import wraps
from time import perf_counter

# from decorator_pbar_threadpool import looping_bar_while_running
from decorator_pbar_async import looping_bar_while_running


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} function was called {count} time")
        return

    return inner


def add(a: int, b: int = 10) -> int:
    """
    return the addition of  a + b
    """
    return a + b


def timed(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ",".join(all_args)
        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}\n")
        return result

    return inner


def calc_recursive_fib(n):
    return 1 if n <= 2 else calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)


@timed
@looping_bar_while_running(desc="Computing fib", cycle_seconds=3.0, tick_seconds=0.1, unit="ticks")
def fib_recursive(n):
    return calc_recursive_fib(n)


if __name__ == "__main__":
    print("***Decorators***")
    print("-------------------\n")
    # print(help(add))
    # Few new commands to inspect functions
    # inspect.getsource, inspect.signature, inspect.signature().parameters
    print(inspect.signature(add))
    print(add(1), add(2), add(3))
    print(inspect.signature(add).parameters)
    print(inspect.getsource(add))
    print(f"Fib number: {fib_recursive(38)}")
