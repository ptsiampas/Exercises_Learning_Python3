# Count how many words occur in a list up to and including the first occurrence of the word “sam”.
# (Write your unit tests for this case too. What if “sam” does not occur?)
__author__ = 'petert'

import sys

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if expected == actual:
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(count_upto_sam(["jack","john","sam","henry"]),3)
    test(count_upto_sam(["jack","john","fred","henry"]),4)


def count_upto_sam(xs):
    count = 0
    for word in xs:
        if word != "sam":
            count += 1
        else:
            break
    if word == "sam":
        count += 1

    return count


test_suite()