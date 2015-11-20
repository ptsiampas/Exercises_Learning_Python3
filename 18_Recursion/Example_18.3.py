from unit_tester import test


def r_sum(nested_number_list):
    tot = 0
    for element in nested_number_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot


def r_max(nxs):
    """
        Find the maximum in a recursive structure of lists within other lists.
        Precondition: No lists or sublists are empty.
    :param nxs: list
    :return:
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False
    return largest


print(r_sum([1, 2, 3, [11, 13], 8]))

test(r_max([2, 9, [1, 13], 8, 6]), 13)
test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]), 100)
test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]), 100)
test(r_max(["joe", ["sam", "ben"]]), "sam")
