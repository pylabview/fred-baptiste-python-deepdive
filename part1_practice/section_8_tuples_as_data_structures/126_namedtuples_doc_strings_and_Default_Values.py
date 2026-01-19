from collections import namedtuple
from random import randint, random

Point2D = namedtuple("Point2D", "x y")

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")


def my_func(a, b=10, c=10):
    print(a, b, c)


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red, blue, green, alpha


Color = namedtuple("Color", "red blue green alpha")

if __name__ == "__main__":
    pt = Point2D(10, 10)
    print(pt)
    print(f"Point.x__doc__ : {Point2D.x.__doc__}")
    print(f"Point.y__doc__ : {Point2D.y.__doc__}")
    print(f"help(Point2D)\n{help(Point2D)}")
    print("------------------------")
    Point2D.__doc__ = "2D cartesian coordinate"
    Point2D.x.__doc__ = "x coordinate"
    Point2D.y.__doc__ = "y coordinate"
    print(help(Point2D))
    print(my_func(1))
    print(my_func.__defaults__)
    my_func.__defaults__ = (1, 10, 10)
    print(my_func())
    print(help(Vector2D))
    print(Vector2D.__new__.__defaults__)
    Vector2D.__new__.__defaults__ = (0, 0)
    print(Vector2D.__new__.__defaults__)
    v1 = Vector2D(10, 10, 10, 10)
    print(v1)
    print("--------------Named Tuples App - Returning multiple values-----")
    color = random_color()
    red, blue, green, alpha = color
    print(f"color: {color}, red = {red} blue = {blue} green {green} alpha {alpha}")
    color = Color(*color)
    print(color)