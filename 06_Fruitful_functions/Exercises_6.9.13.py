# Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2).
# Be sure your implementation of slope can pass the following tests:
#
# test(slope(5, 3, 4, 2), 1.0)
# test(slope(1, 2, 3, 2), 0.0)
# test(slope(1, 2, 3, 3), 0.5)
# test(slope(2, 4, 1, 2), 2.0)
#
# Then use a call to slope in a new function named intercept(x1, y1, x2, y2) that returns the y-intercept of the
# line through the points (x1, y1) and (x2, y2)
#
# test(intercept(1, 6, 3, 12), 3.0)
# test(intercept(6, 1, 1, 6), 7.0)
# test(intercept(4, 6, 12, 8), 5.0)

import sys
import math

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)

# Online whacky solution, found on redit, written in java script. so I converted it.
# var ydelta = y2 - y1;
# var xdelta = x2 - x1;
# var delta;
#
# if (xdelta != 0) {
#   delta = ydelta / xdelta;
# } else {
#   delta = tan(89.99999 * Math.PI / 180);
#   if (y2 < y1) delta = tan(179.99999 * Math.PI / 180);
# }
def slope(x1, y1, x2, y2):
    """ m = (y2-y1)/(x2-x1) ref: http://mathforum.org/cgraph/cslope/calculate.html
        Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the
        points (x1, y1) and (x2, y2).
    """
    ydelta = (y1 - y2)
    xdelta = (x1 - x2)

    if xdelta !=0:
        delta=float(ydelta) / xdelta        # I had originally done the whole thing as a float, but I just needed
                                            # to only do one side of the equation to convert it to a double.
    else:
        delta = math.tan(89.99999 * math.pi / 180)
        if y2 < y1:
            delta = math.tan(269.9999 * math.pi / 180)
    return delta


def intercept(x1, y1, x2, y2):          # google: calculate the x and y intercepts of a line for more invo
    """
    Use a call to slope in a new function named intercept(x1, y1, x2, y2) that returns the y-intercept of the
    line through the points (x1, y1) and (x2, y2)
    Equation: y = mx + b
    """
    m = slope(x1,y1, x2, y2)
    result = y2 - m * x2
    return result

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(slope(5, 3, 4, 2), 1.0)
    test(slope(1, 2, 3, 2), 0.0)
    test(slope(1, 2, 3, 3), 0.5)
    test(slope(2, 4, 1, 2), 2.0)
    test(intercept(1, 6, 3, 12), 3.0)
    test(intercept(6, 1, 1, 6), 7.0)
    test(intercept(4, 6, 12, 8), 5.0)

test_suite()        # Here is the call to run the tests

# print slope(5, 3, 4, 2)
# print slope(1, 2, 3, 2)
# print slope(1, 2, 3, 3)
# print slope(2, 4, 1, 2)
# print intercept(1, 6, 3, 12)
# print intercept(6, 1, 1, 6)
# print intercept(4, 6, 12, 8)