#
# Write a function that helps answer questions like Today is Wednesday. I leave on holiday in 19 days time.
# What day will that be? So the function must take a day name and a delta argument  the number of days to add
# and should return the resulting day name:
# test(day_add("Monday", 4),  "Friday")
# test(day_add("Tuesday", 0), "Tuesday")
# test(day_add("Tuesday", 14), "Tuesday")
# test(day_add("Sunday", 100), "Tuesday")
#
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

def day_add(d_name, length_time):
    st_day=day_num(d_name)
    rtr = day_name((length_time + st_day) % 7)
    return rtr


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_add("Monday", 4),  "Friday")
    test(day_add("Tuesday", 0), "Tuesday")
    test(day_add("Tuesday", 14), "Tuesday")
    test(day_add("Sunday", 100), "Tuesday")


test_suite()        # Here is the call to run the tests