import math


def is_factor(f, n):
    if (n % f) == 0:
        return True
    return False


def is_prime(nu):
    # we only need to check up to the square root of the number,
    # since after that we are just checking the same  in reverse
    max_check = math.ceil(math.sqrt(nu))
    for num in range(2, max_check):
        if is_factor(num, nu):
            return False
    return True


def primes_lessthan(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result

print(primes_lessthan(100))