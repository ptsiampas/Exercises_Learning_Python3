# What will num_digits(0) return? Modify it to return 1 for this case. Why does a call to num_digits(-24)
# result in an infinite loop? (hint: -1//10 evaluates to -1) Modify num_digits so that it works correctly with any
# integer value.
# Add these tests:
# test(num_digits(0), 1)
# test(num_digits(-12345), 5)

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
    test(num_digits(0), 1)
    test(num_digits(1), 1)
    test(num_digits(-12345), 5)

def num_digits(n):
    if n == 0:          # FixMe if its 0 then its always going to be 1 digit, stops while loop atm, needs fixing.
        return 1
    count = 0
    n=abs(n)            # Handle Negative Numbers
    while n != 0:
        count = count + 1
        n = n // 10
    return count

test_suite()