# Adapt the queens program so that we keep a list of solutions that have already printed, so that we don’t print
# the same solution more than once.
from queens_functions import *


def main():
    import random
    rng = random.Random()  # Instantiate a generator
    solutions = []
    bd = list(range(8))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 5:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd not in solutions:
                print("Found solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                solutions.append(bd[:])
                num_found += 1

main()
