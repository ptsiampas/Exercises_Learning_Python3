# Write a function to count how many odd numbers are in a list.
__author__ = 'petert'

def c_odd(xs):
    count=0
    for nu in xs:
        if (nu % 2) != 0:
            count+=1
    return count

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("the number of odd numbers are {0}.".format(c_odd(numbers)))