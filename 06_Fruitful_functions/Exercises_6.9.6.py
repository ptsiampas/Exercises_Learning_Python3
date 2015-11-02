# Write a function days_in_month which takes the name of a month, and returns the number of days in the month.
# Ignore leap years:
#
# test(days_in_month("February"), 28)
# test(days_in_month("December"), 31)


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

def days_in_month(m_day):
    mon_to_days = {
        "January" : 31,
        "February" : 28,
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31,
    }
    return mon_to_days.get(m_day,None)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(days_in_month("February"), 28)
    test(days_in_month("December"), 31)
    test(days_in_month("Dec"), None)



test_suite()        # Here is the call to run the tests