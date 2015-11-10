# 2. Modify the queens program to solve some boards of size 4, 12, and 16. What is the maximum size puzzle you can
# usually solve in under a minute?

from queens_functions import *
import random
import time

def solve_queen(b_size):
    rng = random.Random()  # Instantiate a generator

    bd = list(range(b_size))  # Generate the initial permutation
    tries = 0
    while True:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            return [bd, tries]


def main():

    for size in range(4, 20, 2):
        t0 = time.clock()
        bd_tr = solve_queen(size)
        t1 = time.clock()
        print("{3}x{3} Board: Found solution {0} in {1} tries, in {2:.4f} seconds.".
              format(bd_tr[0], bd_tr[1], t1 - t0, size))


main()
