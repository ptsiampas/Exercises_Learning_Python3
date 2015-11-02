#
# Write a function which is given an exam mark, and it returns a string  the grade for that mark  according to
# this scheme:
# Mark      Grade
# >= 75     First
# [70-75)   Upper Second
# [60-70)   Second
# [50-60)   Third
# [45-50)   F1 Supp
# [40-45)   F2
# < 40      F3
#
# The square and round brackets denote closed and open intervals. A closed interval includes the number,
# and open interval excludes it. So 39.99999 gets grade F3, but 40 gets grade F2. Assume
# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
# Test your function by printing the mark and the grade for all the elements in this list.
#
__author__ = 'petert'

def pmark(mark,level):
    print("Mark(%5.2f), Grade:%s" % (mark, level))

def grade(mark):
    if mark >= 75:
        pmark(mark, "First")
    elif mark >= 70:
        pmark(mark, "Upper Second")
    elif mark >=60:
        pmark(mark, "Second")
    elif mark >=50:
        pmark(mark, "Third")
    elif mark >= 45:
        pmark(mark, "F1 Supp")
    elif mark >=40:
        pmark(mark, "F2")
    elif mark < 40:
        pmark(mark, "F3")


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for m in xs:
    grade(m)

