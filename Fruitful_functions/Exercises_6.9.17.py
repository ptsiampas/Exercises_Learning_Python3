# Write is_multiple to satisfy these unit tests:
# test(is_multiple(12, 3), True)
# test(is_multiple(12, 4), True)
# test(is_multiple(12, 5), False)
# test(is_multiple(12, 6), True)
# test(is_multiple(12, 7), False)
# Can you find a way to use is_factor in your definition of is_multiple?
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

def is_factor(f, n):
    if (n % f) == 0:
        return True
    return False

def is_multiple(n, f):
    return is_factor(f, n)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_multiple(12, 3), True)
    test(is_multiple(12, 4), True)
    test(is_multiple(12, 5), False)
    test(is_multiple(12, 6), True)
    test(is_multiple(12, 7), False)


test_suite()        # Here is the call to run the tests