# Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above, where the first
# item of the pair is the angle to turn, and the second item is the distance to move forward. Set up a list of
# pairs so that the turtle draws a house with a cross through the centre, as show here. This should be done without
# going over any of the lines / edges more than once, and without lifting your pen.

__author__ = 'petert'
import turtle

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes

dg=turtle.Turtle()
dg.pensize(4)
dg.speed(1)

house=[(90, 50),(-45,50),(-90,50),(-135,73),(145,90),(-145,73),(215,90),(-125,53)]

for (tu , st) in house:
    dg.left(tu)
    dg.forward(st)

turtle.mainloop()