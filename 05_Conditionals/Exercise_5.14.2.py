#
# You go on a wonderful holiday (perhaps to jail, if you dont like happy exercises) leaving on day number
# 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for
# the starting day number, and the length of your stay, and it will tell you the name of day of the week
# you will return on.
#
__author__ = 'petert'

#dstay=input("Enter Days of stay? ")
snum=3
dstay=137


for i in range(dstay):
    dnum=snum
    snum+=1
    if snum == 7:
        snum=0

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
