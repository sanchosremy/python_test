"""Constructors
"""


# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
class Point:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 30)
point.name = 12
print(point.name)
