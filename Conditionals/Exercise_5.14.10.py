#
# Write a function find_hypot which, given the length of two sides of a right-angled triangle, returns the
# length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)
#
__author__ = 'petert'

def find_hypot(c1,c2):
    hpot=((c1**2)+(c2**2))**0.5
    return hpot

print("Hypotenus of 10, 12 = %0.3f" % (find_hypot(10,12)))
