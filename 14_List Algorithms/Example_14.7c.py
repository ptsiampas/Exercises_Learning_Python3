from unit_tester import test
from queens_functions import *

# 7|_|_|_|_|_|X|_|_|
# 6|X|_|_|_|_|_|_|_|
# 5|_|_|_|_|X|_|_|_|
# 4|_|X|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|X|
# 2|_|_|X|_|_|_|_|_|
# 1|_|_|_|_|_|_|X|_|
# 0|_|_|_|X|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(has_clashes([6, 4, 2, 0, 5, 7, 1, 3]), False)  # Solution from above

# 7|_|_|_|_|_|X|_|_|
# 6|_|X|_|_|_|_|_|_|
# 5|_|_|_|_|X|_|_|_|
# 4|X|_|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|X|
# 2|_|_|X|_|_|_|_|_|
# 1|_|_|_|_|_|_|X|_|
# 0|_|_|_|X|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]), True)  # Swap rows of first two

# 3|_|_|_|X|
# 2|_|_|X|_|
# 1|_|X|_|_|
# 0|X|_|_|_|
# _|0|1|2|3|
test(has_clashes([0, 1, 2, 3]), True)  # Try small 4x4 board
# 3|_|_|X|_|
# 2|X|_|_|_|
# 1|_|_|_|X|
# 0|_|X|_|_|
# _|0|1|2|3|
test(has_clashes([2, 0, 3, 1]), False)  # Solution to 4x4 case
