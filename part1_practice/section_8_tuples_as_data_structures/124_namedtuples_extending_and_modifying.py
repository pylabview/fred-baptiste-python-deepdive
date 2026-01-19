from collections import namedtuple

Point2D = namedtuple("Point2D", "x y")

Stock = namedtuple("Stock", "symbol year month day open high low close")


if __name__ == "__main__":
    pt = Point2D(10, 20)
    print(f"pt {pt}")
    print(f"pt.x {pt.x}")
    pt = Point2D(100, pt.y)
    print(f"new pt {pt}")
    print("-------------Stock-------------")
    djia = Stock("DJIA", 2018, 1, 25, 26_313, 25_458, 25_260, 26_393)
    print(f"dija {djia}")
    print("Modifying close value")
    djia = Stock(djia.symbol, djia.year, djia.month, djia.day, djia.open, djia.high, djia.low, 1000)
    print(
        "djia = Stock(djia.symbol, djia.year, djia.month, djia.day, djia.open, djia.high, djia.low, 1000)"
    )
    print(f"new djia {djia}")
    *values, _ = djia
    print(f"values is a list because is returned from unpacking{values}")
    values.append(26_393)  # returning back the value of close from 1000 to 26,393
    djia = Stock(
        *values
    )  # Need to pass the positional args with start (*) to unpack the 8 values, not 1
    print(f"Returning back the close value {djia}")
    a = [1, 2, 3]
    print(f"a: {a}, id(a): {id(a)}")
    a = a + [4, 5]
    print(
        f"a = a + [4,5] -> a: {a}, id(a): {id(a)}"
    )  # We are creating a different object, so different men address
    a.append(6)
    print(
        f"Now let's see the address of a -> a: {a}, id: {id(a)}"
    )  # address is the same, more efficient
    # For multiple values, use extend
    a.extend([7, 8, 9])
    print(f"Let's use extend to add multiple vales \n  a.extend([7,8,9]): {a}")
    print("Let's use now the method replace to modify named tuples fields")
    print(f"djia id before mod: djia {djia}, {id(djia)}")
    djia._replace(year=2019, open=125_000)
    print("djia was modified djia.replace(year=2019, open = 125_000)")
    print(djia, id(djia))  # looks like is the same?
    print("Then, let's use the make function, it is a class method")
    stock_value = djia[:7]
    print(f"stock_value = djia[:7], returns a tuple: {stock_value} ")
    print("Let's use the make class metthod to change the close to 1000")
    djia = Stock._make((*stock_value, (100,)))
    print(f"djia = Stock._make(stock_value, (100,)) {djia}")
    print("How can we extend the name tuple")
    print(f"Stock fields, {Stock._fields}")
    StockExt = namedtuple("StockExt", Stock._fields + ("previous_close",))
    print(" StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))")
    print(StockExt._fields)
    print(pt)
    Point3D = namedtuple("Point3D", Point2D._fields + ("z",))
    print(Point3D._fields)
    pt3d = Point3D(*pt, 100)
    print(pt3d)
    djia_ext = StockExt(*djia, 1_000_000)
    print(f"djia_ext: {djia_ext}")
    print(help(StockExt))
