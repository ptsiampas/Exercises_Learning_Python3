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
