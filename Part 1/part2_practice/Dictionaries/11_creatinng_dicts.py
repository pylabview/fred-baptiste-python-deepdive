a = {"k1": 100, "k2": 200}
print(type(a))
print(hash((1, 2, 3)))
t1 = 1, 2, 3
t2 = 1, 2, 3
print(f"hash(t1) == hash(t2) : {hash(t1) == hash(t2)}")
d = {(1, 2, 3): "This is a tuple"}
print(f"d [(1,2,3)] ; {d[(1, 2, 3)]} ")
print(f"Now t1 is t2: {id(t1) is id(t2)}")
print("functions are also hashable")


def my_func(a, b, c):
    print(a, b, c)


def fn_add(a, b):
    return a + b


def fn_inv(a):
    return 1 / a


def fn_mult(a, b):
    return a * b


print(f"hash(my_func): {hash(my_func)}")
d = {my_func: [1, 2, 3]}
print(d)

funcs = {fn_add: (20, 10), fn_inv: (10,), fn_mult: (10, 20)}

for f in funcs:
    print(f)

for f in funcs:
    result = f(*funcs[f])
    print(result)

# Other ways to create dicts is using the constructor class
d1 = {"x": 10, "y": 20}
print(d1)

# We just need to pass an iterable with pair elements, one is the key, the other in the value

d2 = dict([("x", 10), ["y", 20]])

print(d2)
# shallow and depp copy
d3 = {"a": 1, "b": [1, 2, 3, 4], "c": {"cc": 100}}

d4 = dict(d3)
print(f"d3 id : {id(d3)} d4 id : {id(d4)}")
d3["c"]["cc"] = 1000
print(d3, d4)
d3["b"].append(5)
d3["c"]["dd"] = 200
print(d3, d4)
# let's do some dict comprehension
keys = ["a", "b", "c"]
values = (1, 2, 3)
d5 = zip(keys, values)
print(type(d5))
d6 = {k: v for k, v in zip(keys, values)}
print(d6)
keys = "abcd"
values = range(1, 5)
x_coordinates = (-2, -1, 0, 1, 2)
y_coordinates = (-2, -1, 0, 1, 2)
from math import hypot

grid_coordinates_dict = {(x, y): hypot(x, y) for x, y in zip(x_coordinates, y_coordinates)}
print(grid_coordinates_dict)
print(f"grid_coordinates_dict[(-2,-2) -> dist to origin : {grid_coordinates_dict[(-2, -2)]}")
# From key method
d7 = dict.fromkeys("abcd", {})
print(d7)
