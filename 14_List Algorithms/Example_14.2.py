from unit_tester import test


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs - Linear Search Algorithm"""
    for (i, v) in enumerate(xs):
        if v == target:         # Is referred to as a probe.
            return i
    return -1

# Test Cases first
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
test(search_linear(friends, "Zoe"), 1)
test(search_linear(friends, "Joe"), 0)
test(search_linear(friends, "Paris"), 6)
test(search_linear(friends, "Bill"), -1)
