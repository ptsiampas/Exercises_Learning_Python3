# Write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the
# lengths of the two legs as parameters:
#
# test(hypotenuse(3, 4), 5.0)
# test(hypotenuse(12, 5), 13.0)
# test(hypotenuse(24, 7), 25.0)
# test(hypotenuse(9, 12), 15.0)
__author__ = 'petert'
import sys

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

def hypotenuse(c1, c2):
    result = ((c1**2) + (c2**2))**0.5
    return result

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(hypotenuse(3, 4), 5.0)
    test(hypotenuse(12, 5), 13.0)
    test(hypotenuse(24, 7), 25.0)
    test(hypotenuse(9, 12), 15.0)

test_suite()        # Here is the call to run the tests