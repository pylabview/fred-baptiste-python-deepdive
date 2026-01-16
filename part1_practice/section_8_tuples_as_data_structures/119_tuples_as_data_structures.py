from math import sqrt
from random import uniform


def my_func():
    pass


def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x**2 + random_y**2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    return random_x, random_y, is_in_circle


if __name__ == "__main__":
    print("Tuples as data structures")
    london = "London", "UK", 8_780_000
    beijing = "Beijing", "China", 21_000_000
    new_york = "New Your", "US", 8_500_000
    print(london)
    cities = london, beijing, new_york
    print(cities)
    total_population = sum(city[2] for city in cities)
    print(f"Total cities population: {total_population}")
    record = "TSLA", 2019, 1, 10, 432_987, 450_898, 400_876, 445_785
    symbol, year, moth, day, open_, high, low, close = record
    print(f"symbol: {symbol}")
    sym, *_, close_ = record
    print(sym, close_, _)
    print("------------")
    for city, country, population in cities:
        print(city, country, population)
    print("Using enumerate function ")
    for index, city in enumerate(cities):
        print(index, city)
    print("Calculating pi")
    num_attempts = 2_000_000
    count_inside = 0
    for _i in range(num_attempts):
        *_, is_in_circle = random_shot(1)
        if is_in_circle:
            count_inside += 1

    print(f"Pi is approx. : {4 * count_inside / num_attempts}")
