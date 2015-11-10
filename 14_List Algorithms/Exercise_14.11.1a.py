# The section in this chapter called Alice in Wonderland, again! started with the observation that the merge algorithm
# uses a pattern that can be reused in other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:
#
# a. Return only those items that are present in both lists.
from unit_tester import test


def both_inlists(xs, ys):
    """ a. Return only those items that are present in both lists. """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:        # found a match append it
            result.append(xs[xi])
            yi += 1
        elif xs[xi] < ys[yi]:        # move past this item
            xi += 1
        else:
            yi += 1


test(both_inlists([1, 2, 3, 4, 5, 12, 15, 20], [2, 5, 6, 7, 8, 9, 12]), [2, 5, 12])
test(both_inlists([1, 2, 3], [2, 5, 6, 7, 8, 9, 12]), [2])
test(both_inlists([1, 2, 3, 4, 5, 12, 15, 20], [2, 5]), [2, 5])
test(both_inlists([1, 2], []), [])
