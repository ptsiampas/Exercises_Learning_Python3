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

def turn_clockwise(direction):

    if direction == "N":
        dir_change = "E"
    elif direction == "E":
        dir_change = "S"
    elif direction == "S":
        dir_change = "W"
    elif direction == "W":
        dir_change = "N"
    else:
        dir_change = None

    return  dir_change

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N"), "E")
    test(turn_clockwise("W"), "N")
    test(turn_clockwise(42), None)
    test(turn_clockwise("rubbish"), None)


test_suite()        # Here is the call to run the tests
