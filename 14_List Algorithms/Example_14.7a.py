from unit_tester import test
from queens_functions import *

# 5_|_|_|_|_|_|
# 4_|_|_|_|_|_|
# 3_|_|_|_|_|_|
# 2_|_|_|_|_|X|
# 1_|_|_|_|_|_|
# 0_|_|X|_|_|_|
# _0|1|2|3|4|5|
test(share_diagonal(5, 2, 2, 0), False)

# 5_|_|_|_|_|_|
# 4_|_|_|_|_|_|
# 3_|_|_|_|_|_|
# 2_|_|_|_|_|X|
# 1_|_|_|_|_|_|
# 0_|_|_|X|_|_|
# _0|1|2|3|4|5|
test(share_diagonal(5, 2, 3, 0), True)

# 5_|_|_|_|_|_|
# 4_|_|_|_|_|_|
# 3_|_|_|_|X|_|
# 2_|_|_|_|_|X|
# 1_|_|_|_|_|_|
# 0_|_|_|_|_|_|
# _0|1|2|3|4|5|
test(share_diagonal(5, 2, 4, 3), True)

# 5_|_|_|_|_|_|
# 4_|_|_|_|_|_|
# 3_|_|_|_|_|_|
# 2_|_|_|_|_|X|
# 1_|_|_|_|X|_|
# 0_|_|_|_|_|_|
# _0|1|2|3|4|5|
test(share_diagonal(5, 2, 4, 1), True)

# 5|_|_|_|_|_|X|
# 4|_|_|_|_|_|_|
# 3|_|_|_|_|_|_|
# 2|_|_|_|_|_|_|
# 1|_|_|_|_|_|_|
# 0|X|_|_|_|_|_|
# _|0|1|2|3|4|5|
test(share_diagonal(0, 0, 5, 5), True)
