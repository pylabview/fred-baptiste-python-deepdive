import fractions
import math
import sys
from collections import namedtuple
from pprint import pprint
from types import ModuleType


def func():
    a = 10
    b = 10
    math.sqrt(a)
    fractions.Fraction(2, 3)

    print(locals())
    return a, b


if __name__ == "__main__":
    print("Modules, is just another type of object")
    print(f"{func}, {id(func)}")
    # Namespace hold references for all object labels
    print(globals())
    print(globals()["func"]())
    # Namespaces are dictionaries
    print(f"{globals()['math']}, {globals()['fractions']}")
    type(sys.modules)
    print("-------")
    print(f"{sys.modules['math']}")
    print("-------")
    pprint(f"{math.__dict__}", width=40)
    pprint(f"{fractions.__dict__['__file__']}", indent=2)
    print(isinstance(fractions, ModuleType))
    mod = ModuleType("test", "This is a module")
    print(f"Is mod an instance of ModuleType? {isinstance(mod, ModuleType)}")
    mod.hello = lambda: "Hello"
    hello = mod.hello
    hello()
    print(mod.hello())
    print("hello" in globals())
    print("mod" in globals())
    mod.point = namedtuple("Point", "x y")
    p1 = mod.point(10, 10)
    p2 = mod.point(0, 0)
    print(p1, p2)
    print(dir(mod))
    PT = mod.__dict__["point"]
    print(PT(20, 20))
