# Write the function f2c(t) designed to return the integer value of the nearest degree Celsius for given
# temperature in Fahrenheit. (hint: you may want to make use of the built-in function, round.
# Try printing round.__doc__ in a Python shell or looking up help for the round function, and
# experimenting with it until you are comfortable with how it works.)
#
# test(f2c(212), 100)     # Boiling point of water
# test(f2c(32), 0)        # Freezing point of water
# test(f2c(-40), -40)     # Wow, what an interesting case!
# test(f2c(36), 2)
# test(f2c(37), 3)
# test(f2c(38), 3)
# test(f2c(39), 4)

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

def f2c(t):
    """
    (F  -  32)  x  5/9 = C
    """
    cels = round((t - 32) * 5.0 / 9)
    return cels

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(f2c(212), 100)     # Boiling point of water
    test(f2c(32), 0)        # Freezing point of water
    test(f2c(-40), -40)     # Wow, what an interesting case!
    test(f2c(36), 2)
    test(f2c(37), 3)
    test(f2c(38), 3)
    test(f2c(39), 4)


test_suite()        # Here is the call to run the tests