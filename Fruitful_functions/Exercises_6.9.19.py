# Now do the opposite of 6.9.18: write the function c2f which converts Celcius to Fahrenheit:
#
# test(c2f(0), 32)
# test(c2f(100), 212)
# test(c2f(-40), -40)
# test(c2f(12), 54)
# test(c2f(18), 64)
# test(c2f(-48), -54)

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

def c2f(t):
    """
    C  x  9/5 + 32 = F
    """
    cels = round((t * 9.0 / 5 +32))
    return cels


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(c2f(0), 32)
    test(c2f(100), 212)
    test(c2f(-40), -40)
    test(c2f(12), 54)
    test(c2f(18), 64)
    test(c2f(-48), -54)


test_suite()        # Here is the call to run the tests