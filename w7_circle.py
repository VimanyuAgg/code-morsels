import math


class Circle_after:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        print("radius setter called")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = radius

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, d):
        print("diameter setter called")
        self.radius = d / 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    def __repr__(self):
        return "Circle({})".format(self._radius)