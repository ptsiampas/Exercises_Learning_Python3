# 4. Chess boards are symmetric: if we have a solution to the queens problem, its mirror
# solution — either flipping the board on the X or in the Y axis, is also a solution. And
# giving the board a 90 degree, 180 degree, or 270 degree rotation is also a solution. In
# some sense, solutions that are just mirror images or rotations of other solutions — in the
# same family — are less interesting than the unique “core cases”. Of the 92 solutions for
# the 8 queens problem, there are only 12 unique families if you take rotations and mirror
# images into account. Wikipedia has some fascinating stuff about this.
#     (e) Now adapt the queens program so it won’t list solutions that are in the same family.
#     It only prints solutions from unique families.
from unit_tester import test
from queens_functions import *
from itertools import permutations

def main():
    import random
    rng = random.Random()  # Instantiate a generator
    solutions = []
    bd = list(range(8))  # Generate the initial permutation
    num_found = 0
    tries = 0
    #n = 8
    #cols = range(n)
    while num_found < 5:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd not in solutions:
                print("Found unique solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                solutions.extend(generate_sym(bd))
                print(solutions)
                num_found += 1
    print(len(solutions))


main()
