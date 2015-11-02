#
# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a function which is given the day number, and it returns the day name (a string)
#
__author__ = 'petert'

dnum=input("Enter Day number? ")

if dnum == 0:
    print("Sunday")
elif dnum == 1:
    print("Monday")
elif dnum == 2:
    print("Tuesday")
elif dnum == 3:
    print("Wedensday")
elif dnum == 4:
    print("Thursday")
elif dnum == 5:
    print("Friday")
elif dnum == 6:
    print("Saturday")
else:
    print("Invalid Choice")