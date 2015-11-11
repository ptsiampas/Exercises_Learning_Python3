def test(actual, expected):
    import sys
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
               .format(linenum, expected, actual))
    print(msg)


def timing(f, n, a):
    """
    Times a function.
    :param f: Function to time.
    :param n: number of times to run it.
    :param a: data for the function.
    :return:
    """
    import time
    print(f.__name__, end=": ")

    t1 = time.clock()
    for i in range(n):
        for x in range(10):
            f(a)

    t2 = time.clock()
    print(round(t2 - t1, 3))
