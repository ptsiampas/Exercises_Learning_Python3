# 5. Write a function, recursive_min, that returns the smallest value in a nested number
# list. Assume there are no empty lists or sublists:
from unit_tester import test


def recursive_min(list):
    smallest = None
    first_time = True
    for n in list:
        if isinstance(n, type([])):
            val = recursive_min(n)
        else:
            val = n

        if first_time or val < smallest:
            smallest = val
            first_time = False
    return smallest


test(recursive_min([2, 9, [1, 13], 8, 6]), 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]), 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]), -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]), -13)
