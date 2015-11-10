# The section in this chapter called Alice in Wonderland, again! started with the observation that the merge algorithm
# uses a pattern that can be reused in other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:
# d. Return items that are present in either the first or the second list.

from unit_tester import test


def in_both_lists(xs, ys):
    """
    d. Return items that are present in either the first or the second list
    :param xs: First List
    :param ys: Second List
    :return: Return items that are present in either the first or the second list
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
        elif xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
    return result

test(in_both_lists([1, 2, 3, 4], [2, 5, 6, 8]), [1, 2, 3, 4, 5, 6, 8])
test(in_both_lists([2, 5, 6, 8], [1, 2, 3, 4]), [1, 2, 3, 4, 5, 6, 8])
test(in_both_lists([2, 5, 6, 8], [1, 4]), [1, 2, 4, 5, 6, 8])
test(in_both_lists([2, 5, 6, 8], []), [2, 5, 6, 8])
test(in_both_lists([], [2, 5, 6, 8]), [2, 5, 6, 8])
test(in_both_lists([], []), [])