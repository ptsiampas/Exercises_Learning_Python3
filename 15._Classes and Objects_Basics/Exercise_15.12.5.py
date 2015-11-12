# 5. Given four points that fall on the circumference of a circle, find the midpoint of the circle.
# When will you function fail?
#
# Hint: You must know how to solve the geometry problem before you think of going
# anywhere near programming. You cannot program a solution to a problem if you don’t
# understand what you want the computer to do!

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

    def find_circle_centre(self, pt2, pt3, pt4):
        # Find the mid point between the two sets.
        mid1 = self.halfway(pt2)
        mid2 = Point(pt3).halfway(pt4)

        return mid1


# Main part

test(Point(5, 5).find_circle_centre(Point(6, -2), Point(6, -2), Point(2, -4)), (2, 1))
