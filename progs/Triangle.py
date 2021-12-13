import math
from Point import Point
from Point import PointError


class TriangleError(PointError):
    pass


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        try:
            self.__triangle = [
                Point(p.getx(), p.gety()) for p in [vertice1, vertice2, vertice3]
            ]
        except AttributeError:
            raise TriangleError

    def perimeter(self):
        d12 = self.__triangle[0].distance_from_point(self.__triangle[1])
        d23 = self.__triangle[1].distance_from_point(self.__triangle[2])
        d13 = self.__triangle[0].distance_from_point(self.__triangle[2])
        return d12 + d23 + d13


try:
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())

    triangle = Triangle("blah", "blah", "blah")

except TriangleError:
    print("Sorry, I can't do that")
