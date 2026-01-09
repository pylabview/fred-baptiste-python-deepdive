## Decorators ##
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} called at {run_dt}")
        return result

    return inner


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for (k, v) in kwargs.items()]
        all_str = args_ + kwargs_
        args_str = ",".join(all_str)
        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run")
        return result

    return inner


def dec_1(fn):
    def inner():
        print("Running dec 1")
        return fn()

    return inner


def dec_2(fn):
    def inner():
        print("Running dec 2")
        return fn()

    return inner


def dec_11(fn):
    def inner():
        result = fn()
        print("Running dec 11")
        return result

    return inner


def dec_22(fn):
    def inner():
        result = fn()
        print("Running dec 22")
        return result

    return inner


############################################################################


@dec_1
@dec_2
def my_func():
    print(f"Running {my_func.__name__}")


@dec_11
@dec_22
def my_func2():
    print(f"Running {my_func2.__name__}")


@logged
def func1():
    pass


@logged
def func2():
    pass


@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    result = reduce(mul, range(1, n + 1))
    print(result)
    return result


def main():
    func1()
    func2()
    fact(3)
    fact(6)
    my_func()
    my_func2()


if __name__ == "__main__":
    print("Hello, this is Decorator Coding, section 7.109")
    main()
