#
# Write the inverse function day_num which is given a day name, and returns its number:
# test(day_num("Friday"), 5)
# test(day_num("Sunday"), 0)
#test(day_num(day_name(3)), 3)
# test(day_name(day_num("Thursday")), "Thursday")
#
import sys


__author__ = 'petert'


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
    test(day_num("Friday"), 5)
    test(day_num("Sunday"), 0)
    test(day_num(day_name(3)), 3)
    test(day_name(day_num("Thursday")), "Thursday")
    test(day_num("Halloween"), None)


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


def day_num(day):
    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    else:
        return None

test_suite()        # Here is the call to run the tests
