#
# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the
# triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return
# True if the triangle is right-angled, or False otherwise.
#
__author__ = 'petert'

def find_hypot(c1,c2):
    hpot=((c1**2)+(c2**2))**0.5
    return hpot

def is_rightangled(side1, side2, side3):
    hypot_test=find_hypot(side1,side2)
    if abs(hypot_test - side3) < 0.000001:
        print("Triangle is at right angle",abs(hypot_test - side3))
    else:
        print("truangle is NOT a right angle",abs(hypot_test - side3))

is_rightangled(3,4,5)
is_rightangled(18,8,20)