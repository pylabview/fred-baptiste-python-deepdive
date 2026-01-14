from datetime import datetime, timezone
from fractions import Fraction


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
