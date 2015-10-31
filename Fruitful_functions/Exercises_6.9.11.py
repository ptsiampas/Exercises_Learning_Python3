# Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b
#
# test(compare(5, 4), 1)
# test(compare(7, 7), 0)
# test(compare(2, 3), -1)
# test(compare(42, 1), 1)


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

def compare(n1,n2):
    if n1 > n2:
        return 1
    elif n1 == n2:
        return 0
    elif n1 < n2:
        return -1
    return None

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(compare(5, 4), 1)
    test(compare(7, 7), 0)
    test(compare(2, 3), -1)
    test(compare(42, 1), 1)



test_suite()        # Here is the call to run the tests