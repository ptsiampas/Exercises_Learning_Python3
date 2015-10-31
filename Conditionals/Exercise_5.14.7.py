#
# Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.
#

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()            # Added this line
    t.penup()               # Added for Exercise 5.14.7
    t.forward(10)
    t.pendown()             # Added for Exercise 5.14.7

turtle.setup(640,480)
tess = turtle.Turtle()       # Create tess and set some attributes
tess.penup()
tess.setposition(-190, -150)
tess.pendown()
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

turtle.done()
