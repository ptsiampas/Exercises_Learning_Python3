def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # CXalc the absolute x distance
    return dx == dy  # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
    with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False  # No clashes - col c has a safe placement


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


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
    transposed = bd[:]
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
    result.append(bd[:])
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

    return remove_dups(result)
