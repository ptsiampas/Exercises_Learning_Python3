# Sum all the elements in a list up to but not including the first even number.
# (Write your unit tests. What if there is no even number?)
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

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sum_upto_first_even([1,3,2]),4)
    test(sum_upto_first_even([1,3,3]),7)
    test(sum_upto_first_even([2,3,3]),0)

def sum_upto_first_even(xs):
    final=0
    for num in xs:
        if num%2 != 0:
            final+=num
        else:
            break
    return final


test_suite()