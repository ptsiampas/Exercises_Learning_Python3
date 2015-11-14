# 5. In games, we often put a rectangular “bounding box” around our sprites. (A sprite is an
# object that can move about in the game, as we will see shortly.) We can then do collision
# detection between, say, bombs and spaceships, by comparing whether their rectangles
# overlap anywhere.
# Write a function to determine whether two rectangles collide. Hint: this might be quite a
# tough exercise! Think carefully about all the cases before you code.

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

    def find_circle_centre(self, pt2, pt3, pt4):  # TODO: find_circle_center not working.
        # Ref: http://www.regentsprep.org/regents/math/geometry/gcg6/RCir.htm
        # (x - h)^2 + (y - k)^2 = r^2
        # (h, k) = Centre of the circle.
        #
        # Search: how to find the center of a circle with 3 points
        # Find the Slope for the two lines.
        mr = (self.y - pt2.y) / (self.x - pt2.x)
        mt = (pt3.y - pt4.y) / (pt3.x - pt4.x)

        # Find the mid point between the two lines r and t.
        mrx = (self.x + pt2.x) / 2
        mry = (self.y + pt2.y) / 2
        mtx = (pt3.y + pt4.y) / 2
        mty = (pt3.y + pt4.y) / 2

        # Solve for y
        y = 5

        # Solve for x
        x = (mr * mt)
        return (x, mr, mt, mrx, mry, mtx, mty)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def flip(self):
        self.height += self.width
        self.width = self.height - self.width
        self.height -= self.width

    def contains(self, pt):
        """
        Original code before I compressed it:
        cx = self.corner.x
        cy = self.corner.y
        ex = float(pt.x)
        ey = float(pt.y)

        if cx <= ex < self.width:
            x = True
        else:
            x = False

        if cy <= ey < self.height:
            y = True
        else:
            y = False
        return x and y
        :param pt: Point to check
        :return: if its within the rectangle
        """
        return (self.corner.x <= float(pt.x) < self.width) \
               and (self.corner.y <= float(pt.y) < self.height)


r = Rectangle(Point(), 10, 5)
test(r.contains(Point(0, 0)), True)
test(r.contains(Point(3, 3)), True)
test(r.contains(Point(3, 7)), False)
test(r.contains(Point(3, 5)), False)
test(r.contains(Point(3, 4.99999)), True)
test(r.contains(Point(-3, -3)), False)
