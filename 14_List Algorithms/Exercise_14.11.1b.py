# The section in this chapter called Alice in Wonderland, again! started with the observation that the merge algorithm
# uses a pattern that can be reused in other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:
# b. Return only those items that are present in the first list, but not in the second.
from unit_tester import test

def infirstlist(xs, ys):
    """
    b. Return only those items that are present in the first list, but not in the second.
    :param xs: Sorted list A
    :param ys: Sorted List B
    :return: Return only those items that are present in the first list, but not in the second.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):           # we have come to the end of the second list.
            result.extend(xs[xi:])  # dump the rest of the array, since we know it's not in the second list.
            return result

        if xs[xi] not in ys:        # its not in the second list
            result.append(xs[xi])
        else:
            yi += 1

        xi += 1

test(infirstlist([1, 2, 3, 4], [2, 4, 6, 8]), [1, 3])
test(infirstlist([1, 2, 3, 4, 5, 6, 7], [2]), [1, 3, 4, 5, 6, 7])
test(infirstlist([1, 2, 3, 4, 5, 6, 7], []), [1, 2, 3, 4, 5, 6, 7])
test(infirstlist([], []), [])
