# 14. Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is
# an even number and False if it is odd.
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
    test(is_even(0),True)
    test(is_even(1),False)
    test(is_even(2),True)
    test(is_even(3),False)

    test(is_odd(0),False)
    test(is_odd(1),True)
    test(is_odd(2),False)
    test(is_odd(3),True)

def is_even(n):
    if (n % 2) == 0:
        return True
    return False

# 15. Now write the function is_odd(n) that returns True when n is odd and False otherwise.
#     Include unit tests for this function too.
def is_odd(n):
    #if (n % 2) != 0:
    #    return True
    # Finally, modify it so that it uses a call to is_even to determine if its argument is an
    # odd integer, and ensure that its test still pass.
    if is_even(n) == True:
        return False
    return True

test_suite()        # Here is the call to run the tests