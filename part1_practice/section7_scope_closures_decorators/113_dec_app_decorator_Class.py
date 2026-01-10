def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print(f"decorator function called a={a},  b= {b}")
            return fn(*args, **kwargs)

        return inner

    return dec


@my_dec(10, 20)
def my_func(s):
    print(f"Hello {s}")


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print(f"called a={self.a} b={self.b} c={c}")


class MyClass_dec:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("dec called -> a={a} b={b}")
            return fn(*args, **kwargs)

        return inner


@MyClass_dec(1000, 2000)
def my_func_dec_class(s):
    print(f"Hello {s}")


if __name__ == "__main__":
    print("Dec classes")
    print("my_func function")
    print("---------")
    print(my_func("Rodrigo"))
    print("decorating with class in the long way")
    obj = MyClass(10, 20)
    print(obj(100))
    print("-------")
    print(my_func_dec_class("Rodrigo"))