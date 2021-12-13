import math


class PointError(AttributeError, ValueError):
    pass


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        try:
            self.__point = (float(x), float(y))
        except AttributeError or ValueError:
            raise PointError

    def getx(self):
        return self.__point[0]

    def gety(self):
        return self.__point[1]

    def distance_from_xy(self, x, y):
        return math.dist(self.__point, (float(x), float(y)))

    def distance_from_point(self, point):
        try:
            return math.dist(self.__point, (point.getx(), point.gety()))
        except AttributeError:
            raise PointError


if __name__ == "__main__":
    try:
        point1 = Point(0, 0)
        point2 = Point(1, 1)
        print(point1.distance_from_point(point2))
        print(point2.distance_from_xy(2, 0))

        point3 = "Blah"
        print(point1.distance_from_point(point3))
    except PointError:
        print("Sorry, I can't do that")
