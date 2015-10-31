# Write a function, is_prime, which takes a single integer argument and returns True when the argument is a
# prime number and False otherwise. Add tests for cases like this:
#
# test(is_prime(11), True)
# test(is_prime(35), False)
# test(is_prime(19911121), True)
#
# The last case could represent your birth date. Were you born on a prime day? In a class of 100 students,
# how many do you think would have prime birth dates?

import sys
import math

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


def is_factor(f, n):
    if (n % f) == 0:
        return True
    return False

def is_prime(nu):
    # we only need to check up to the square root of the number,
    # since after that we are just checking the same  in reverse
    max_check = math.ceil(math.sqrt(nu))
    for num in range(2,max_check):
        if is_factor(num,nu):
            return False
    return True

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(is_prime(11), True)
    test(is_prime(37), True)
    test(is_prime(35), False)
    test(is_prime(19911121), True)
    test(is_prime(19680514), False)

test_suite()