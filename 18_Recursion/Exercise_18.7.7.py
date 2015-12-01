# 7. Write a function flatten that returns a simple list containing all the values in a nested list:
#
# test(flatten([2,9,[2,1,13,2],8,[2,6]]),[2,9,2,1,13,2,8,2,6])
# test(flatten([[9,[7,1,13,2],8],[7,6]]),[9,7,1,13,2,8,7,6])
# test(flatten([[9,[7,1,13,2],8],[2,6]]),[9,7,1,13,2,8,2,6])
# test(flatten([['this',['a',['thing'],'a'],'is'],['a','easy']]),
#               ['this','a','thing','a','is','a','easy'])
# test(flatten([]), [])
from unit_tester import test


def flatten(list):
    flat_list = []
    for item in list:
        # Recusive case
        if isinstance(item, type([])):
            flat_list.extend(flatten(item))
        else:
            # Base Case
            flat_list.append(item)
    return flat_list


def main():
    test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]), [2, 9, 2, 1, 13, 2, 8, 2, 6])
    test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]), [9, 7, 1, 13, 2, 8, 7, 6])
    test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]), [9, 7, 1, 13, 2, 8, 2, 6])
    test(flatten([['this', ['a', ['thing'], 'a'], 'is'], ['a', 'easy']]),
         ['this', 'a', 'thing', 'a', 'is', 'a', 'easy'])
    test(flatten([]), [])


if __name__ == '__main__':
    main()
