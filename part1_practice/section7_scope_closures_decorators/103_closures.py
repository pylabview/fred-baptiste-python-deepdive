# 103_closure.py


def outer():
    x = "python"

    def inner():
        print(x)

    return inner


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def outer_ext():
    count = 0

    def inner1():
        nonlocal count
        count += 1
        return count

    def inner2():
        nonlocal count
        count += 1
        return count

    return inner1, inner2


def pow(n):
    def inner(x):
        return x**n

    return inner


# Creating multiple closures in a loop
def create_adders():
    adders = []
    for n in range(1, 5):  # adding 1 to 4 to a number x
        adders.append(lambda x: x + n)
    return adders


def create_adders_fixed():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders


if __name__ == "__main__":
    print("03. Closures")
    fn = outer()
    print(fn.__code__.co_freevars)
    print(f"{fn.__closure__}")
    c = counter()
    print(f"counter  function freevars {c.__code__.co_freevars}")
    print(f"count closure checks {c.__closure__}")
    print(f"Calling c multiple times: {c(), c(), c()}")
    print(" Let's see how we share same freevar in one funtion")
    fn1, fn2 = outer_ext()
    print(f"freevars {fn1.__code__.co_freevars, fn2.__code__.co_freevars}")
    print(f"calling fn1, fn1, fn2 {fn1(), fn1(), fn2()}")
    print("Multiple closure instances")
    square = pow(2)
    cube = pow(3)
    print(
        "Now let's have a function that use a freevar to store a value and extend its use with different user inputs"
    )
    print(f"square and cube based on x**n: {square(2), cube(3)}")
    adders = create_adders()
    print(
        f"adders[0](10), adders[1](10), adders[2](10), adders[3](10): {adders[0](10), adders[1](10), adders[2](10), adders[3](10)} "
    )
    print(f"{adders[0].__code__.co_freevars}")
    adders_fixed = create_adders_fixed()
    print(
        f"adders_fixed[0](10), adders_fixed[1](10), adders_fixed[2](10), adders_fixed[3](10): {adders_fixed[0](10), adders_fixed[1](10), adders_fixed[2](10), adders_fixed[3](10)} "
    )
