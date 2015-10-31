# Which of these tests fail? Explain why.
#
# test(3 % 4, 0)
# test(3 % 4, 3)
# test(3 / 4, 0)
# test(3 // 4, 0)
# test(3+4  *  2, 14)
# test(4-2+2, 0)
# test(len("hello, world!"), 13)

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
    test(3 % 4, 0)    # Failed because 3 % 4 is 3 not 0
    test(3 % 4, 3)
    test(3 / 4, 0)
    test(3 // 4, 0)
    test(3+4  *  2, 14)  # Failed becuase of operator priority, fix would be (3+4)*2
    test(4-2+2, 0)       # Failed because of sequence of operator, if 0 is the answer then 4-(2+2)
    test(len("hello, world!"), 13)


test_suite()        # Here is the call to run the tests