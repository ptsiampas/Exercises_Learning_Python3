# e. Return items from the first list that are not eliminated by a matching element in the second list. In this case,
#    an item in the second list “knocks out” just one matching item in the first list. This operation is sometimes
#    called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]
from unit_tester import test

def bagdiff(xs, ys):
    """
    e. Return items from the first list that are not eliminated by a matching element in the second list. In this case,
       an item in the second list “knocks out” just one matching item in the first list. This operation is sometimes
       called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]
    :param xs: Sorted list A
    :param ys: Sorted List B
    :return: Return items from the first list that are not eliminated by a matching element in the second list.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1


test(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]), [5, 11, 11, 12, 13])
test(bagdiff([5, 7, 11, 11, 11, 12, 13, 20], [7, 8, 11, 20]), [5, 11, 11, 12, 13])
