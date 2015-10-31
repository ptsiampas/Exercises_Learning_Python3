# Write three functions that are the inverses of to_secs (6.9.7-8):
#
# 1. hours_in returns the whole integer number of hours represented by a total number of seconds.
# 2. minutes_in returns the whole integer number of left over minutes in a total number of seconds, once
#    the hours have been taken out.
# 3. seconds_in returns the left over seconds represented by a total number of seconds.
# You may assume that the total number of seconds passed to these functions is an integer.
#  Here are some test cases:
# test(hours_in(9010), 2)
# test(minutes_in(9010), 30)
# test(seconds_in(9010), 10)


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

def hours_in(se):
    """hours_in returns the whole integer number of hours represented by a total number of seconds."""
    hrs=int(se/60/60)
    return hrs

def minutes_in(se):
    """
    minutes_in returns the whole integer number of left over minutes in a total number of seconds, once
    the hours have been taken out.
    """
    r_min=(se/60)%60
    return r_min

def seconds_in(se):
    """seconds_in returns the left over seconds represented by a total number of seconds."""
    sec = se % 60
    return sec

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(hours_in(9010), 2)
    test(minutes_in(9010), 30)
    test(seconds_in(9010), 10)



test_suite()        # Here is the call to run the tests