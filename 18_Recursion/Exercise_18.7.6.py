# 6. Write a function count that returns the number of occurrences of target in a nested
# list:
from unit_tester import test


def count_old(obj, list):
    counter = 0
    first_time = True
    for item in list:
        if isinstance(item, type([])):
            result = count(obj, item)
            counter = result
            print("List count({0},{1})={2}".format(obj, item, result))
        else:
            print("Not List counter={0}, obj={1}, item={2}".format(counter, obj, item))

        if first_time or item == obj:
            print("first time counter={0}, obj={1}, item={2}".format(counter, obj, item))
            counter += 1
            first_time = False
    return counter


def count(search_obj, list):
    counter = 0

    for item in list:
        # Recursive Case - Want to first check if the item is a list
        if isinstance(item, type([])):
            counter += count(search_obj, item)
        else:  # Ok its not a list lets check if it the search object matches
            # Base Case - Does not CALL it's self
            if item == search_obj:
                counter += 1

    return counter


def stdCount(obj, list):
    counter = 0
    for item in list:
        if item == obj:
            counter += 1
    return counter


# test(stdCount(7, [9, 7, 1, 13, 2, 8, 7, 6]), 2)

test(count(2, []), 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]), 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]), 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]), 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]), 6)
test(count('a', [['this', ['a', ['thing', 'a'], 'a'], ' is '], ['a', 'easy']]), 4)
