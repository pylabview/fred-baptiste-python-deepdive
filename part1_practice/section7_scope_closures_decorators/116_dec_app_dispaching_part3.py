from collections.abc import Sequence
from functools import singledispatch

# from decimal import Decimal
from html import escape
from numbers import Integral


def my_func():
    pass


@singledispatch  # this is the defualt function
def htmlize(a):
    return escape(str(a))


@htmlize.register(Integral)
def _(a):
    return f"{a}(<i>{str(hex(a))}</i>)"


@htmlize.register(Sequence)
def _(l):
    items = (f"<li>{htmlize(item)}</li>" for item in l)
    return "<ul>\n" + "\n".join(items) + "\n</ul>"


@htmlize.register(str)
def _(s):
    return escape(s).replace("\n", "<br/>\n")


@htmlize.register(tuple)
def _(t):
    items = (f"{escape(str(item))}" for item in t)
    return f"({', '.join(items)})"


if __name__ == "__main__":
    print("Decorator Application: Dispatching Part 2")
    print(f"htmlize.registry -> {htmlize.registry}")
    print(f"htmlize.dispatch(str) -> {htmlize.dispatch(str)}")
    print(f"htmlize.dispatch(int) -> {htmlize.dispatch(int)}")
    print(f"htmlize.dispatch(bool) -> {htmlize.dispatch(bool)}")
    print("--------")
    print(htmlize(10), htmlize(True))
    print("--------")
    print(htmlize([1, 2, 3]))
    print(
        htmlize("""
                  Python Rock!
                  x : 10 < n
                  """)
    )
    print(htmlize((1, 2, 3, 4)))
