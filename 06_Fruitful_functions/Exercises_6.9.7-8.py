# 7. Write a function to_secs that converts hours, minutes and seconds to a total number of seconds.
# Here are some tests that should pass:
#
# test(to_secs(2, 30, 10), 9010)
# test(to_secs(2, 0, 0), 7200)
# test(to_secs(0, 2, 0), 120)
# test(to_secs(0, 0, 42), 42)
# test(to_secs(0, -10, 10), -590)
#
# 8. Extend to_secs so that it can cope with real values as inputs. It should always return an integer number of seconds
# (truncated towards zero):
#
# test(to_secs(2.5, 0, 10.71), 9010)
# test(to_secs(2.433,0,0), 8758)

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

def to_secs(hr,mi,se):
    hr_2_sec = hr * 60 * 60
    mi_2_sec = mi * 60
    total_sec = int(hr_2_sec + mi_2_sec + se) # Added for 8. int type conversion.
    return total_sec

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(to_secs(2, 30, 10), 9010)
    test(to_secs(2, 0, 0), 7200)
    test(to_secs(0, 2, 0), 120)
    test(to_secs(0, 0, 42), 42)
    test(to_secs(0, -10, 10), -590)
    test(to_secs(2.5, 0, 10.71), 9010)
    test(to_secs(2.433,0,0), 8758)

test_suite()        # Here is the call to run the tests