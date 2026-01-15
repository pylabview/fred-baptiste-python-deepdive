from datetime import datetime, timezone
from fractions import Fraction
from functools import total_ordering
from math import sqrt


def my_func():
    pass

def dec_speak(cls):
    cls.speak = lambda self, message: f"{self.__class__.__name__} says {message}"
    return cls


def obj_info(self):
    results = []
    results.append(f"time: {datetime.now(timezone.utc)}")
    results.append(f"Class: {self.__class__.__name__}")
    results.append(f"Mem ID: {id(self)}")
    for k, v in vars(self).items():
        results.append(f"{k}: {v}")
    return results


def debug_info(cls):
    cls.debug = obj_info
    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return "Hello there!"


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

        @property
        def speed(self):
            return self._speed

        @speed.setter
        def speed(self, new_speed):
            if new_speed > top_speed:
                raise ValueError(f"Speed cannot exceed top speed: {self.top_speed}")
            else:
                self._speed = new_speed


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, value):
        if isinstance(value, Point):
            return self.x == value.x and self.y == value.y
        else:
            return False

    def __lt__(self, value):
        if isinstance(value, Point):
            return abs(self) < abs(value)
        else:
            return NotImplemented


"""
Now, although we could proceed in a similar way and define `>=`, `<=` and `>` 
using the same technique, observe that if `<` and `==` is defined then:

* `a <= b` iff `a < b or a == b`
* `a > b` iff `not(a<b) and a != b`
* `a >= b` iff `not(a<b)`
        
        
"""


def complete_ordering(cls):
    if "__eq__" in dir(cls) and "__lt__" in dir(cls):
        cls.__le__ = lambda self, value: self < value or self == value
        cls.__gt__ = lambda self, value: not (self < value) and not (self == value)
        cls.__ge__ = lambda self, value: not (self < value)
    return cls


@complete_ordering
class PointDec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, value):
        if isinstance(value, PointDec):
            return self.x == value.x and self.y == value.y
        else:
            return False

    def __lt__(self, value):
        if isinstance(value, PointDec):
            return abs(self) < abs(value)
        else:
            return NotImplemented


@total_ordering
class PointDecBuildIn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, value):
        if isinstance(value, PointDecBuildIn):
            return self.x == value.x and self.y == value.y
        else:
            return False

    def __lt__(self, value):
        if isinstance(value, PointDecBuildIn):
            return abs(self) < abs(value)
        else:
            return NotImplemented


if __name__ == "__main__":
    print("class decorator")
    Fraction = dec_speak(Fraction)
    f = Fraction(2, 3)
    print(f.speak("Hello"))
    Person = dec_speak(Person)
    p = Person("John", 1939)
    print(p.speak("this works!!!"))
    print(p.debug())
    favorite = Automobile("toyota", "Highlander", 2025, 70)
    print(favorite.debug())
    p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)
    print(f"p1 == p2: {p1 == p2}")
    print(f"p3 < p1: {p3 < p1}")
    p5, p6, p7, p8 = PointDec(2, 3), PointDec(2, 3), PointDec(0, 0), PointDec(100, 200)
    print(f"p5 {p5} p6 {p6} p7{p7} p8{p8}")
    print(f"p5 <= p8: {p5 <= p8}")
    print(f"p8 >= p6: {p8 >= p6}")
    print(f"p5 != p6: {p5 != p6}")
    print("------Now using the build in dec total_ordering form functools")
    p9, p10, p11, p12 = (
        PointDecBuildIn(2, 3),
        PointDecBuildIn(2, 3),
        PointDecBuildIn(0, 0),
        PointDecBuildIn(100, 200),
    )
    print(f"p9 {p5} p10 {p6} p11{p7} p12{p8}")
    print(f"p9 <= p12: {p9 <= p12}")
    print(f"p12 >= p10: {p12 >= p10}")
    print(f"p9 != p10: {p9 != p10}")