# Sum up all the even numbers in a list.
__author__ = 'petert'

def is_negative(n):
    if n < 0:
        return True
    return False

def sum_even(xs):
    final=0
    for num in xs:
        if is_negative(num):
            final+=num
    return final

numbers=[1,-2,3,-4]

print("Sum of all the negative numbers is {0}".format(sum_even(numbers)))

