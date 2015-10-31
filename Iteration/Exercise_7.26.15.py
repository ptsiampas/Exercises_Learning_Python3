# Write a function num_even_digits(n) that counts the number of even digits in n. These tests should pass:
#
# test(num_even_digits(123456), 3)
# test(num_even_digits(2468), 4)
# test(num_even_digits(1357), 0)
# test(num_even_digits(0), 1)

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
    test(num_even_digits(123456), 3)
    test(num_even_digits(2468), 4)
    test(num_even_digits(1357), 0)
    test(num_even_digits(0), 1)

def is_even(n):
    if (n % 2) == 0:
        return True
    return False

def num_even_digits(n):
    if n == 0:          # FixMe if its 0 then its always going to be 1 digit, stops while loop atm, needs fixing.
        return 1
    count = 0
    n=abs(n)            # Handle Negative Numbers
    while n != 0:
        if is_even(n):
            count = count + 1
        n = n // 10
    return count


test_suite()