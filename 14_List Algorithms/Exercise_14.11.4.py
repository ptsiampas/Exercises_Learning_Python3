# 4. Chess boards are symmetric: if we have a solution to the queens problem, its mirror
# solution — either flipping the board on the X or in the Y axis, is also a solution. And
# giving the board a 90 degree, 180 degree, or 270 degree rotation is also a solution. In
# some sense, solutions that are just mirror images or rotations of other solutions — in the
# same family — are less interesting than the unique “core cases”. Of the 92 solutions for
# the 8 queens problem, there are only 12 unique families if you take rotations and mirror
# images into account. Wikipedia has some fascinating stuff about this.
#     (a) Write a function to mirror a solution in the Y axis,
#     (b) Write a function to mirror a solution in the X axis,
#     (c) Write a function to rotate a solution by 90 degrees anti-clockwise, and use this to
#         provide 180 and 270 degree rotations too.
#     (d) Write a function which is given a solution, and it generates the family of symmetries
#         for that solution. For example, the symmetries of [0,4,7,5,2,6,1,3] are
#           [[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
#           [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
#           [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
#           [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]]
#     (e) Now adapt the queens program so it won’t list solutions that are in the same family.
#     It only prints solutions from unique families.
from unit_tester import test


def mirror_x(bd):
    m_size = len(bd) - 1
    result = []
    for pos in range(m_size + 1):
        result.append(m_size - bd[pos])
    return result


def mirror_y(bd):
    # alternate way of reversing the list is to do:
    # return bd[::-1]
    bd.reverse()
    return bd


def rot_90(bd):
    # Transpose the array first
    transposed = bd.copy()
    for x in range(len(bd)):
        y = bd[x]
        transposed[y] = x

    # Mirror it on Y axis
    return mirror_y(transposed)


def rot_180(bd):
    return rot_90(rot_90(bd))


def rot_270(bd):
    return rot_180(rot_90(bd))


def remove_dups(seq):
    # order preserving
    noDupes = []
    [noDupes.append(i) for i in seq if not noDupes.count(i)]
    return noDupes


def generate_sym(bd):
    result = []
    syms_generated = []
    result.append(bd.copy())
    result.append(rot_270(bd))
    result.append(rot_180(bd))
    result.append(rot_90(bd))
    result.append(rot_90(mirror_x(bd)))
    result.append(mirror_y(bd))
    result.append(mirror_x(bd))
    result.append(mirror_y(mirror_x(bd)))
    result.append(rot_180(mirror_x(bd)))
    result.append(rot_270(mirror_x(bd)))
    result.append(mirror_x(mirror_y(bd)))
    result.append(rot_90(mirror_y(bd)))
    result.append(rot_180(mirror_y(bd)))
    result.append(rot_270(mirror_y(bd)))
    syms_generated.extend(remove_dups(result))
    return syms_generated


# Solution:
# [SOL=[0,4,7,5,2,6,1,3], R270[7,1,3,0,6,4,2,5],
# R180[4,6,1,5,2,0,3,7],R90=[2,5,3,1,7,4,6,0],
# MY[3,1,6,2,5,7,4,0],R90(MX)[0,6,4,7,1,3,5,2],
# MX[7,3,0,2,5,1,6,4],R270(MX)[5,2,4,6,0,3,1,7]]

board = [5, 7, 1, 3, 0, 6, 4, 2]

# test(rot_90(board), [2, 5, 3, 1, 7, 4, 6, 0])
# test(rot_180(board), [4, 6, 1, 5, 2, 0, 3, 7])
# test(rot_270(board), [7, 1, 3, 0, 6, 4, 2, 5])
# test(mirror_x(board), [7, 3, 0, 2, 5, 1, 6, 4])
# test(mirror_y(board), [3, 1, 6, 2, 5, 7, 4, 0])

print(generate_sym(board))
