# Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk pirate makes a turn,
# and then takes some steps forward, and repeats this. Our social science student now records pairs of data:
# the angle of each turn, and the number of steps taken after the turn. Her experimental data is
# [(160, 20), (-43, 10), (270, 8), (-43, 12)].
# Use a turtle to draw the path taken by our drunk friend.

__author__ = 'petert'
import turtle

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes

dg=turtle.Turtle()

for (tu , st) in [(160, 20), (-43, 10), (270, 8), (-43, 12)]:
    dg.left(tu)
    dg.forward(st)

turtle.mainloop()