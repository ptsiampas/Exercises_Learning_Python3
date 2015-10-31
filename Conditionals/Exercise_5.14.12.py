#
# Extend the above program from Ex. 5.14.11 so that the sides can be given to the function in any order.
#
__author__ = 'petert'

def find_hypot(c1,c2):
    hpot=((c1**2)+(c2**2))**0.5
    return hpot

def is_rightangled(side_1, side_2, side_3):

    if side_1 > side_2:          # FixMe I couldn't work this out myself, I found a simple Algorithm and modified
        if side_1 > side_3:      # Found here: http://www.programiz.com/article/algorithm-programming
            lside = side_1
            s1_side = side_2
            s2_side = side_3
        else:
            lside = side_3
            s1_side = side_1
            s2_side = side_2
    else:
        if side_2 > side_3:
            lside = side_2
            s1_side = side_3
            s2_side = side_1
        else:
            lside = side_3
            s1_side = side_1
            s2_side = side_2

    hypot_test=find_hypot(s1_side,s2_side)

    if abs(hypot_test - lside) < 0.000001:
        print("Triangle is at right angle")
    else:
        print("Triangle is NOT a right angle")

is_rightangled(3,5,4)
is_rightangled(20,5,8)