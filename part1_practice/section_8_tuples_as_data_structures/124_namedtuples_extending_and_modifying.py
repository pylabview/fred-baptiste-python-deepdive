from collections import namedtuple


def greetings():
    print("Hello namedtuples extending and modifying")


Point2D = namedtuple("Point2D", "x y")
Stock = namedtuple("Stock", "symbol year month day open high low close")

if __name__ == "__main__":
    greetings()
    pt = Point2D(10, 20)
    print(f"pt {pt}, pt id: {id(pt)}")
    pt = Point2D(100, pt.y)
    print(f"pt {pt}, pt id: {id(pt)}")
    djia = Stock("DJIA", 2018, 1, 25, 26_313, 26_458, 26_260, 26_392)
    print(f"djia: {djia}")
    *values, close = djia
    print(f"*values: {values}, close: {close}")
    djia = Stock(*values, 1000)
    print(f"Modifying close value to 1000: {djia}")