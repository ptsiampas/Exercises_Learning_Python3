# The section in this chapter called Alice in Wonderland, again! started with the observation that the merge algorithm
# uses a pattern that can be reused in other situations. Adapt the merge algorithm to write each of these functions,
# as was suggested there:
#
# a. Return only those items that are present in both lists.
# b. Return only those items that are present in the first list, but not in the second.
# c. Return only those items that are present in the second list, but not in the first.
# d. Return items that are present in either the first or the second list.
# e. Return items from the first list that are not eliminated by a matching element in the second list. In this case,
#    an item in the second list “knocks out” just one matching item in the first list. This operation is sometimes
#    called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]
from unit_tester import test

def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):           # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result           # And we're done.

        if yi >= len(ys):           # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

def merge_a(xs, ys):
    """ a. Return only those items that are present in both lists. """
    result = []
    xi = 0

    while True:
        if xi >= len(xs):
            return result

        if xs[xi] > ys[len(ys)-1]:
            return result

        if xs[xi] in ys:
            result.append(xs[xi])
            xi += 1
        else:
            xi += 1


# test(merge(['1', '2', '3'], ['5', '6', '7']), ['1', '2', '3', '5', '6', '7'])
# test(merge([], []), [])
test(merge_a([1, 2, 3, 4, 5, 12, 15, 20], [2, 5, 6, 7, 8, 9, 12]), [2, 5, 12])
test(merge_a([1, 2, 3], [2, 5, 6, 7, 8, 9, 12]), [2])
test(merge_a([1, 2, 3, 4, 5, 12, 15, 20], [2, 5]), [2, 5])
# test(merge_a([1, 2], []), [])
