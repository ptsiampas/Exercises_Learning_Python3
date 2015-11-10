# The section in this chapter called Alice in Wonderland, again! started with the observation that the merge algorithm
# uses a pattern that can be reused in other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:
# c. Return only those items that are present in the second list, but not in the first.
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

def insecondlist(xs, ys):
    """
    c. Return only those items that are present in the second list, but not in the first.
    :param xs: First List
    :param ys: Second List
    :return: Return only those items that are present in the second list, but not in the first.
    """
    return infirstlist(ys, xs)     # Cause really, I am lazy :P


test(insecondlist([1, 2, 3, 4, 5, 12, 15, 20], [2, 5, 6, 7, 8, 9, 12]), [6, 7, 8, 9])
test(insecondlist([1, 2, 3], [2, 5, 6, 7, 8, 9, 12]), [5, 6, 7, 8, 9, 12])
test(insecondlist([1, 2, 3, 4, 5, 12, 15, 20], [2, 5]), [])
test(infirstlist([], []), [])