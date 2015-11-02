__author__ = 'petert'
import math

b = ("bob", 19, "CS")       # Tuple Packing
(name, age, studies) = b    # Tuple UnPacking

# Traditional swapping of values
a = 5
b = 10
temp = a
a = b
b = temp

# swapping values with Tuple's
(a, b) = (b, a)


# Return items as a Tuple
def f(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)