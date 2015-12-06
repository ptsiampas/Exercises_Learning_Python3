class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        """ If the left operand of * is a primitive type and the right operand is a Point, Python
        invokes __rmul__, which performs scalar multiplication:
        """
        return Point(other * self.x, other * self.y)

    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


def heading(s):
    """Draws a line under the heading - yes because I am bored"""
    line = ""
    for x in range(len(s)):
        line += "="
    return "{}\n{}".format(s, line)


def multadd(x, y, z):
    return x * y + z


def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))


def main():
    # examples of operator overloading - check the add, mul and rmul definitions
    print(heading("21.8. Operator overloading Examples"))
    p1 = Point(3, 4)
    p2 = Point(5, 7)
    print("Point{} * Point{} = {}".format(p1, p2, p1 * p2))  # Execute mul because the left of the * is a Point.
    print("2 * Point{} = {}".format(p2, 2 * p2))  # Executes rmul because the left operand of * is a primitive.

    print()
    print(heading("21.9. Polymorphism Examples"))
    print("multiadd function = {}".format(multadd(3, 2, 1)))
    print("multiadd function also works with points = {}".format(multadd(2, p1, p2)))
    print("multiadd function also works with points = {}".format(multadd(p1, p2, 1)))
    my_list = [1, 2, 3, 4]
    front_and_back(my_list)
    p = Point(3, 4)
    front_and_back(p)


if __name__ == '__main__':
    main()
