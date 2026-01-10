from functools import lru_cache

def fib_recursive(n):
    print(f"Calculationg fib({n})")
    return 1 if n < 3 else fib_recursive(n - 1) + fib_recursive(n - 2)


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):  # This is the inner function, needs to know the n numbers
        print(f"Calculating fib({n})")
        if (
            n not in cache
        ):  # This is a closure (freevar) because it refers to cache a local variable
            cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return cache[n]

    return calc_fib  # here we return the closure


def memoize_fib(fib):
    cache = {1: 1, 2: 1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)  # Here we are not doing the recursion here in the closure
        return cache[n]

    return inner


@memoize_fib
def fib_recursive_dec(n):
    print(f"Calculationg fib({n})")
    return 1 if n < 3 else fib_recursive_dec(n - 1) + fib_recursive_dec(n - 2)


def memoize(fn):
    cache = dict()

    def inner(n):  # Only takes one argument
        if n not in cache:
            cache[n] = fn(n)  # Here we are not doing the recursion here in the closure
        return cache[n]

    return inner


@memoize
def fib_recursive_mem(n):
    print(f"--> Calculating fib({n})")
    return 1 if n < 3 else fib_recursive_mem(n - 1) + fib_recursive_mem(n - 2)


def fact(n):
    print(f"Calculating {n}!")
    return 1 if n < 2 else n * fact(n - 1)


@memoize
def fact_mem(n):
    print(f"Calculating {n}!")
    return 1 if n < 2 else n * fact_mem(n - 1)

@lru_cache()
def fib_recursive_lru(n):
    print(f"Calculating fib({n})")
    return 1 if n < 3 else fib_recursive_lru(n - 1) + fib_recursive_lru(n - 2)

@lru_cache(maxsize=8)
def fib_recursive_lru_8(n):
    print(f"Calculating fib({n})")
    return 1 if n < 3 else fib_recursive_lru_8(n - 1) + fib_recursive_lru_8(n - 2)


if __name__ == "__main__":
    print("Hello")
    # print("Using recursive fib")
    # fib_recursive(10)
    # print("-----")
    # print("Using cache with classes")
    # f = Fib()
    # print(f.fib(10))
    # print("-----closure-----")
    # f = fib()  # This is the inner function, tha is return and assigned to f
    # print(f(10))  # The inner function needs to know the n value
    # print(f(10))
    # print("-----with decorator-----")
    # print(fib_recursive_dec(10))
    # print(fib_recursive_dec(10))
    # print("-----with memoization-----")
    # print(fib_recursive_mem(10))
    # print("--- Calling the second time ---")
    # print(fib_recursive_mem(10))
    # print("----- calculating fact")
    # print(fact(6))
    # print("---- calculating fact with memoization")
    # print(fact_mem(6))
    # print("--- calling the 2nd time")
    # print(fact_mem(6))
    # print("--- Now calculating factorial of 7")
    # print(fact_mem(7))
    # start = perf_counter()
    # print(fib_recursive_mem(200))
    # stop = perf_counter()
    # print(f"1st time {stop - start:.7f}")
    # print("---- calling the 2nd Fib with memoization")
    # start = perf_counter()
    # print(fib_recursive_mem(200))
    # stop = perf_counter()
    # print(stop - start)
    # print(f"1st time {stop - start:.7f}")
    # print("calling recursive fibonacci with lru_cache ")
    # print(fib_recursive_lru(10))
    print("---- Calling fib with lru size of 8 ")
    print(fib_recursive_lru_8(8))
    print("calling again to calculate fibonacci of 8")
    print(fib_recursive_lru_8(8))
    print("Now lte's calculate fib of 9, will see it just do fib(9)")
    print(fib_recursive_lru_8(9)) 
    print("But fib of 1 fell of the tail")
    print(fib_recursive_lru_8(1))