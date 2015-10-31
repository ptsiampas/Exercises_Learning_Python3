#
# Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values
# between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.
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
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    if a >= 200:                    # Added colour changes for Exercise 5.14.8
        tess.color("blue", "red")
    elif a >=100:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")

    draw_bar(tess, a)

turtle.done()

