# 4. The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients
# a and b completely describe the line. Write a method in the Point class so that if a point
# instance is given another point, it will compute the equation of the straight line joining
# the two points. It must return the two coefficients as a tuple of two values.
#
# For example,
# >>> print(Point(4, 11).get_line_to(Point(6, 15)))
# >>> (2, 3)
#
# This tells us that the equation of the line joining the two points is “y = 2x + 3”. When
# will your method fail?
from unit_tester import test


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distance(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        dsquared = dx * dx + dy * dy
        result = dsquared ** 0.5
        return result

    def reflect_x(self):
        ry = self.y * -1
        return Point(self.x, ry)

    def slope_from_origin(self):
        if self.y == 0 or self.x == 0:
            return 0
        slope = float(self.y) / self.x
        return slope

    def get_line_to(self, target):
        # y = mx + b
        # m is the slope, and b is the y-intercept
        m = (self.y - target.y) / (self.x - target.x)
        b = self.y - (m * self.x)
        return (m, b)


test(Point(4, 11).get_line_to(Point(6, 15)), (2, 3))

