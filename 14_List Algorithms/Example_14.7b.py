from unit_tester import test
from queens_functions import *

# Solutions cases that should not have any clashes
# 7|_|_|_|_|_|_|_|_|
# 6|X|_|_|_|_|_|_|_|
# 5|_|_|_|_|O|_|_|_|
# 4|_|X|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|_|
# 2|_|_|X|_|_|_|_|_|
# 1|_|_|_|_|_|_|_|_|
# 0|_|_|_|X|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([6, 4, 2, 0, 5], 4), False)
# 7|_|_|_|_|_|X|_|_|
# 6|X|_|_|_|_|_|_|_|
# 5|_|_|_|_|X|_|_|_|
# 4|_|X|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|O|
# 2|_|_|X|_|_|_|_|_|
# 1|_|_|_|_|_|_|X|_|
# 0|_|_|_|X|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7), False)

# More test cases that should mostly clash
# 7|_|_|_|_|_|_|_|_|
# 6|_|_|_|_|_|_|_|_|
# 5|_|_|_|_|_|_|_|_|
# 4|_|_|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|_|
# 2|_|_|_|_|_|_|_|_|
# 1|_|O|_|_|_|_|_|_|
# 0|X|_|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([0, 1], 1), True)
# 7|_|_|_|_|_|_|_|_|
# 6|_|O|_|_|_|_|_|_|
# 5|X|_|_|_|_|_|_|_|
# 4|_|_|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|_|
# 2|_|_|_|_|_|_|_|_|
# 1|_|_|_|_|_|_|_|_|
# 0|_|_|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([5, 6], 1), True)
# 7|_|_|_|_|_|_|_|_|
# 6|X|_|_|_|_|_|_|_|
# 5|_|O|_|_|_|_|_|_|
# 4|_|_|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|_|
# 2|_|_|_|_|_|_|_|_|
# 1|_|_|_|_|_|_|_|_|
# 0|_|_|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([6, 5], 1), True)
# 7|_|_|_|_|_|_|_|_|
# 6|_|X|_|_|_|_|_|_|
# 5|_|_|_|_|_|_|_|_|
# 4|_|_|X|_|_|_|_|_|
# 3|_|_|_|O|_|_|_|_|
# 2|_|_|_|_|_|_|_|_|
# 1|_|_|_|_|_|_|_|_|
# 0|X|_|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([0, 6, 4, 3], 3), True)
# 7|_|_|O|_|_|_|_|_|
# 6|_|_|_|_|_|_|_|_|
# 5|X|_|_|_|_|_|_|_|
# 4|_|_|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|_|_|
# 2|_|_|_|_|_|_|_|_|
# 1|_|_|_|_|_|_|_|_|
# 0|_|X|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([5, 0, 7], 2), True)
# 7|_|_|_|_|_|_|_|_|
# 6|_|_|_|_|_|_|_|_|
# 5|_|_|_|_|_|_|_|_|
# 4|_|_|_|_|_|_|_|_|
# 3|_|_|_|O|_|_|_|_|
# 2|X|_|_|_|_|_|_|_|
# 1|_|_|X|_|_|_|_|_|
# 0|_|X|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([2, 0, 1, 3], 1), False)
# 7|_|_|_|_|_|_|_|_|
# 6|_|_|_|_|_|_|_|_|
# 5|_|_|_|_|_|_|_|_|
# 4|_|_|_|_|_|_|_|_|
# 3|_|_|_|X|_|_|_|_|
# 2|X|_|_|_|_|_|_|_|
# 1|_|_|O|_|_|_|_|_|
# 0|_|X|_|_|_|_|_|_|
# _|0|1|2|3|4|5|6|7|
test(col_clashes([2, 0, 1, 3], 2), True)
