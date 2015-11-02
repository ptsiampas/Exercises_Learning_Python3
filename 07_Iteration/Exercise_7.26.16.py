# Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs.
# For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
#
# test(sum_of_squares([2, 3, 4]), 29)
# test(sum_of_squares([ ]), 0)
# test(sum_of_squares([2, -3, 4]), 29)

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

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sum_of_squares([2, 3, 4]), 29)
    test(sum_of_squares([ ]), 0)
    test(sum_of_squares([2, -3, 4]), 29)



def sum_of_squares(xn):
    result=0
    for nu in xn:
        result += (nu**2)
    return result

test_suite()