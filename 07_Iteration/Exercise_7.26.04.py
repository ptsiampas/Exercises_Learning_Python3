# Count how many words in a list have length 5.
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

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(count_words_of_length(["one","two","thre","four"],5),0)
    test(count_words_of_length(["12345","123","123456","12345"],5),2)
    test(count_words_of_length(["12345","12345","12345","12345"],5),4)

def count_words_of_length(xs, l):
    count=0
    for word in xs:
        if len(word) == l:
            count+=1
    return count


test_suite()