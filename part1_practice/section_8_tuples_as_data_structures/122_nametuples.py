from collections import namedtuple


def my_funct():
    pass


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Point3DNice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__} (x={self.x}, y={self.y}, z= {self.z})"

    def __eq__(self, other):
        if isinstance(other, Point3DNice):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


Vector3D = namedtuple("Vector3D", "x y z")


if __name__ == "__main__":
    print("Named Tuples Coding!!")
    Point2D = namedtuple("Point2D", ("x", "y"))
    print(Point2D(2, 3))
    print("---------------")
    pt3d_1 = Point3D(10, 20, 30)
    pt3d_2 = Point3D(10, 20, 30)
    print(f"Printing {pt3d_1}")
    p = Point2D(x=10, y=20)
    print("We need a __repr__ implementation to make it nice")
    print(f"Is p instance of tuple: {isinstance(p, tuple)}")
    p1_2d = Point2D(20, 20)
    p2_2d = Point2D(20, 20)
    print(f"p1_2d is p2_2d: {p1_2d is p2_2d}")
    print(f"p1_2d == p2_2d: {p1_2d == p2_2d} ")
    print("But we cannot do the same for classes")
    print(f"pt3d_1 is pt3d_2: {pt3d_1 is pt3d_2}")
    print(f"pt3d_1 == pt3d_2: {pt3d_1 == pt3d_2}")
    pt3d_1n = Point3DNice(10, 20, 30)
    pt3d_2n = Point3DNice(10, 20, 30)
    print(f"pt3d_1n is pt3d_2n: {pt3d_1n is pt3d_2n}")
    print(f"pt3d_1n == pt3d_2n: {pt3d_1n == pt3d_2n}")
    print(f"pt3d_1n {pt3d_1n}, pt3d_2n {pt3d_2n}")
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(1, 1, 1)
    print(f"v1 {v1}, v2 {v2}, tuple(v1): {tuple[1]}, v1[0:2] {v1[0:2]}, v1.x {v1.x}")
    print(f"pt3_1n.__dict__: {pt3d_1n.__dict__} ")
    print(f"v1._asdict(): {v1._asdict()}")
