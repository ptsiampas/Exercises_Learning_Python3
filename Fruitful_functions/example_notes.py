__author__ = 'petert'
import math

# 6.1. Return values
def area(radius):
    b = 3.14159 * radius ** 2  # Better to use temp var's as it helps with dbugging.
    return b

def absolute_value(x):
    """
    Example of multiple returns in a single function
    :param x: value
    :return: absolute value of x
    """
    if x < 0:
        return -x
    return x

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
           return wd
    return ""

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx * dx + dy * dy
    result = dsquared**0.5
    return result

def distance2(x1, y1, x2, y2):                  # Version 2 using math module
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

# 6,4 Composition
def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print(distance(1, 2, 4, 6))

print(distance2(1, 2, 4, 6))

print(area2(1, 2, 4, 6))


