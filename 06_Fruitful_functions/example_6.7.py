import sys

def absolute_value(x):
    """
    Example of multiple returns in a single function
    :param x: value
    :return: absolute value of x
    """
    if x < 0:
        return 1
    elif x > 0:
        return x

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
    test(absolute_value(17), 17)
    test(absolute_value(-17), 17)
    test(absolute_value(0), 0)
    test(absolute_value(3.14), 3.14)
    test(absolute_value(-3.14), 3.14)

test_suite()        # Here is the call to run the tests