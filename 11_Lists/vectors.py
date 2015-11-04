

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


def add_vectors(u, v):
    # 5. Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write
    # functions to perform standard operations on vectors. Create a script named vectors.py and write Python code to
    # pass the tests in each case.
    #
    # Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns a new list
    # containing the sums of the corresponding elements of each:
    #
    # test(add_vectors([1, 1], [1, 1]), [2, 2])
    # test(add_vectors([1, 2], [1, 4]), [2, 6])
    # test(add_vectors([1, 2, 1], [1, 4, 3]), [2, 6, 4])
    new_list = []

    for x in range(len(u)):
        new_list.append(u[x] + v[x])
    return new_list

def scalar_mult(s, v):
    # 6. Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar
    #  multiple of v by s. :
    #
    # test(scalar_mult(5, [1, 2]), [5, 10])
    # test(scalar_mult(3, [1, 0, -1]), [3, 0, -3])
    # test(scalar_mult(7, [3, 0, 5, 11, 2]), [21, 0, 35, 77, 14])
    new_list = []

    for i in range(len(v)):
        new_list.append(s * v[i])
    return new_list

def dot_product(u, v):
    # 7. Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns the sum
    # of the products of the corresponding elements of each (the dot_product).
    #
    # test(dot_product([1, 1], [1, 1]),  2)
    # test(dot_product([1, 2], [1, 4]),  9)
    # test(dot_product([1, 2, 1], [1, 4, 3]), 12)
    result=0

    for i in range(len(u)):
        result += u[i] * v[i]

    return result

def cross_product(u, v):
    # Extra challenge for the mathematically inclined: Write a function cross_product(u, v) that takes two lists of
    # numbers of length 3 and returns their cross product. You should write your own tests.
    result = 0

    return result

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(add_vectors([1, 1], [1, 1]), [2, 2])
    test(add_vectors([1, 2], [1, 4]), [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]), [2, 6, 4])

    test(scalar_mult(5, [1, 2]), [5, 10])
    test(scalar_mult(3, [1, 0, -1]), [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]), [21, 0, 35, 77, 14])

    test(dot_product([1, 1], [1, 1]),  2)
    test(dot_product([1, 2], [1, 4]),  9)
    test(dot_product([1, 2, 1], [1, 4, 3]), 12)
    test(dot_product([1, 3, -5], [4, -2, -1]), 3)

test_suite()