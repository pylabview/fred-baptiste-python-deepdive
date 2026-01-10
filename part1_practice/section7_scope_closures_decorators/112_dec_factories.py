def timed_n_times(fn, n):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(n):
            start = perf_counter()
            result = fn(*args, **kwargs)
            elapsed = perf_counter() - start
            total_elapsed += elapsed
        avg_run_time = total_elapsed / 10
        print(f"Run time {avg_run_time:0.7f} with {n} repetitions")
        return result

    return inner


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n - 1) + calc_fib_recurse(n - 2)


def fib(n):
    return calc_fib_recurse(n)


def fib_10(n):
    return calc_fib_recurse(n)


def dec(fn):
    print("running dec..")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)

    return inner


def dec_factory_example(a, b):
    print("running dec_factory")

    def dec(fn):
        print("running dec..")

        def inner(*args, **kwargs):
            print("running inner")
            print(f"a = {a} and b = {b}")
            return fn(*args, **kwargs)

        return inner

    return dec


@dec_factory_example(5, 6)
def my_func_factory():
    print("running my_func()!")


def timed(n):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                elapsed = perf_counter() - start
                total_elapsed += elapsed
            avg_run_time = total_elapsed / n
            print(f"Average Run time {avg_run_time:0.7f} with {n} repetitions")
            return result

        return inner

    return dec


@timed(10)
def fib_factory(n):
    return calc_fib_recurse(n)


if __name__ == "__main__":
    # print("Hello")
    # print("Decorating fib in the long way fib = timed(fib)")
    # fib = timed(fib)
    # print(fib(30))
    # print("-------------------------------")
    # print("Using the timed_n_times dec  fib_10 = timed_n_times(fib, 10)")
    # fib_10 = timed_n_times(fib_10, 10)
    # print("Timing fib of 30")
    # print(fib_10(30))
    # print("---- decorating my_func --")
    # print(my_func())
    print("my_func_factory")
    print(my_func_factory())
    print(f"fib of 30: {fib_factory(30)}")
