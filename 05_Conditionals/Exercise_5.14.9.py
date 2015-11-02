#
# In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list
# is negative? Try it out. Change the program so that when it prints the text value for the negative bars,
# it puts the text below the bottom of the bar.
#
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    if height < 0:          # Added if statement for Exercise 5.14.9
        t.penup()           # Note: I don't like the way its being done, think it can be done better.
        t.forward(-14)
        t.write("  "+ str(height))
        t.forward(14)
        t.pendown()
    else:
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

turtle.setup(640,600)
tess = turtle.Turtle()       # Create tess and set some attributes
tess.penup()
tess.setposition(-300, 0)
tess.pendown()
tess.pensize(3)

xs = [48,0, 117,-265, 200,240,160,-101,260,220,-33]  # Added negative numbers Ex. 5.14.9

for a in xs:
    if a >= 200:                    # Added colour changes for Exercise 5.14.8
        tess.color("blue", "red")
    elif a >=100:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")

    draw_bar(tess, a)

turtle.done()