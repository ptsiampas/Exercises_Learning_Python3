# Write a function is_factor(f, n) that passes these tests:
#
# test(is_factor(3, 12), True)
# test(is_factor(5, 12), False)
# test(is_factor(7, 14), True)
# test(is_factor(7, 15), False)
# test(is_factor(1, 15), True)
# test(is_factor(15, 15), True)
# test(is_factor(25, 15), False)
# An important role of unit tests is that they can also act as unambiguous “specifications” of what is expected.
# These test cases answer the question Do we treat 1 and 15 as factors of 15?

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

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_factor(3, 12), True)
    test(is_factor(5, 12), False)
    test(is_factor(7, 14), True)
    test(is_factor(7, 15), False)
    test(is_factor(1, 15), True)
    test(is_factor(15, 15), True)
    test(is_factor(25, 15), False)

test_suite()        # Here is the call to run the tests