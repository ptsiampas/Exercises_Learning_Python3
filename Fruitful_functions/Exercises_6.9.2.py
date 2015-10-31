#
# Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is
# Sunday. Once again, return None if the arguments to the function are not valid. Here are some tests
# that should pass:
# test(day_name(3), "Wednesday")
# test(day_name(6), "Saturday")
# test(day_name(42), None)

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

def day_name(num):
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    else:
        return None

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_name(3), "Wednesday")
    test(day_name(6), "Saturday")
    test(day_name(42), None)



test_suite()        # Here is the call to run the tests