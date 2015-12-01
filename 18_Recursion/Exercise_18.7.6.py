# 6. Write a function count that returns the number of occurrences of target in a nested
# list:
from unit_tester import test

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
