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

    test(replace("Mississippi", "i", "I"), "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

    test(replace(s, "om", "am"),
        "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a"),
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")


def replace(str, old_sub, new_sub):
    # 10. Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s
    return new_sub.join(str.split(old_sub))

test_suite()