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
from queens_functions import *


def main():
    import random
    rng = random.Random()  # Instantiate a generator
    solutions = []
    bd = list(range(8))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 90:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd not in solutions:
                print("Found solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                solutions.append(bd[:])
                num_found += 1

main()
