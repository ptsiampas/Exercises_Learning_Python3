# Every week a computer scientist buys four lotto tickets. She always chooses the same prime numbers, with the hope
# that if she ever hits the jackpot, she will be able to go onto TV and Facebook and tell everyone her secret. This
# will suddenly create widespread public interest in prime numbers, and will be the trigger event that ushers in a new
# age of enlightenment. She represents her weekly tickets in Python as a list of lists:
#
# my_tickets = [ [ 7, 17, 37, 19, 23, 43],
#                [ 7,  2, 13, 41, 31, 43],
#                [ 2,  5,  7, 11, 13, 17],
#                [13, 17, 37, 19, 23, 43] ]
# Complete these exercises.
#     a. Each lotto draw takes six random balls, numbered from 1 to 49. Write a function to return a lotto draw.
#     b. Write a function that compares a single ticket and a draw, and returns the number of correct picks on
#        that ticket:
#         test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]), 3)
#     c. Write a function that takes a list of tickets and a draw, and returns a list telling how many picks were
#        correct on each ticket:
#         test(lotto_matches([42,4,7,11,1,13], my_tickets), [1,2,3,1])
#     d. Write a function that takes a list of integers, and returns the number of primes in the list:
#         test(primes_in([42, 4, 7, 11, 1, 13]), 3)
#     e. Write a function to discover whether the computer scientist has missed any prime numbers in her selection of
#        the four tickets. Return a list of all primes that she has missed:
#         test(prime_misses(my_tickets), [3, 29, 47])
#     f. Write a function that repeatedly makes a new draw, and compares the draw to the four tickets.
#       i. Count how many draws are needed until one of the computer scientist’s tickets has at least 3 correct picks.
#          Try the experiment twenty times, and average out the number of draws needed.
#       ii. How many draws are needed, on average, before she gets at least 4 picks correct?
#       iii. How many draws are needed, on average, before she gets at least 5 correct? (Hint: this might take a while.
#            It would be nice if you could print some dots, like a progress bar, to show when each of the 20 experiments
#            has completed.)
from unit_tester import test
import random
import statistics


def lotto_draw():
    """
    Draws 6 random numbers from a list of numbers.
    a. Each lotto draw takes six random balls, numbered from 1 to 49. Write a function to return a lotto draw.
    :return: returns list of numbers un-sorted.
    """
    draw = list(range(1, 50))
    rng = random.Random()
    rng.shuffle(draw)
    draw = draw[:6]
    return draw


def lotto_match(drawn_numbers, numbers_picked):
    """
    b. Write a function that compares a single ticket and a draw, and returns the number of correct picks on that ticket
    :param drawn_numbers: numbers drawn
    :param numbers_picked: single row of numbers
    :return: the number of matched numbers
    """
    matched_numbers = 0
    drawn_numbers.sort()
    pi = 0
    di = 0
    while True:
        if pi >= len(numbers_picked):
            return matched_numbers

        if di >= len(drawn_numbers):
            return matched_numbers

        if drawn_numbers[di] in numbers_picked:  # its not in the ticket
            matched_numbers += 1
        else:
            pi += 1
        di += 1
    return matched_numbers


def lotto_matches(drawn_numbers, tickets):
    """
    c. Write a function that takes a list of tickets and a draw, and returns a list telling how many picks were correct
    on each ticket
    :param drawn_numbers: list of drawn numbers
    :param tickets: list of each row of numbers.
    :return: list of which tickets were correct.
    """
    correct = []
    for ticket in tickets:
        correct.append(lotto_match(drawn_numbers, ticket))
    return correct


def is_prime(n):
    # internet's most efficient answer for finding prime :)
    from math import sqrt
    from itertools import count, islice
    if n < 2:
        return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if not n % number:
            return False
    return True


def primes_in(int_list):
    """
    d. Write a function that takes a list of integers, and returns the number of primes in the list:
    :param int_list: list of numbers
    :return: returns the number of primes in the list
    """
    c = 0
    for n in int_list:
        if is_prime(n):
            c += 1
    return c


def prime_misses(tickets):
    """
    e. Write a function to discover whether the computer scientist has missed any prime numbers in her selection
       of the four tickets. Return a list of all primes that she has missed
    :param tickets: list of rows that only contains primes
    :return: Return a list of all primes that have been missed
    """
    prime_list = []

    for i in range(1, 50):  # Build a list of primes
        if is_prime(i):
            prime_list.append(i)

    for ticket in tickets:
        for n in ticket:
            if n in prime_list:  # remove it from the prime list
                prime_list.remove(n)

    return prime_list


def weeky_draw(tickets, match_number):
    """
    Write a function that repeatedly makes a new draw, and compares the draw to the four tickets.

    i.   Count how many draws are needed until one of the computer scientist’s tickets has at least 3 correct picks.
         Try the experiment twenty times, and average out the number of draws needed.
    ii.  How many draws are needed, on average, before she gets at least 4 picks correct?
    iii. How many draws are needed, on average, before she gets at least 5 correct? (Hint: this might take a while.
         It would be nice if you could print some dots, like a progress bar, to show when each of the 20 experiments
         has completed.)

    :param tickets:
    :return:
    """
    number_of_draws = 0
    matches = 0

    while matches < match_number:
        for match in lotto_matches(lotto_draw(), tickets):
            if match >= match_number:
                matches += 1
        number_of_draws += 1

    return number_of_draws


def avg_draws(n):
    draw_list = []
    average_draw_list = 0
    for i in range(20):
        draw_list.append(weeky_draw(my_tickets, n))
        average_draw_list = statistics.mean(draw_list)
        print(".")
    print("On {0} matches the number of average draws needed: {1}".format(n, average_draw_list))


my_tickets = [[7, 17, 37, 19, 23, 43],
              [7, 2, 13, 41, 31, 43],
              [2, 5, 7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43]]

test(lotto_match([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]), 3)
test(lotto_matches([42, 4, 7, 11, 1, 13], my_tickets), [1, 2, 3, 1])
test(primes_in([42, 4, 7, 11, 1, 13]), 3)
test(prime_misses(my_tickets), [3, 29, 47])

avg_draws(3)
avg_draws(4)
avg_draws(5)