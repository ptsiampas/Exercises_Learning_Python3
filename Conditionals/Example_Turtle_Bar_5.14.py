# The turtle has a lot more power than weve seen so far. The full documentation can be found
# at http://docs.python.org/py3k/library/turtle.html or within PyScripter, use Help and search for the turtle module.
# Here are a couple of new tricks for our turtles:
#
# We can get a turtle to display text on the canvas at the turtles current position. The method to do
# that is alex.write("Hello").
# We can fill a shape (circle, semicircle, triangle, etc.) with a color. It is a two-step process. First we call
# the method alex.begin_fill(), then we draw the shape, then we call alex.end_fill().
# Weve previously set the color of our turtle  we can now also set its fill color, which need not be the
# same as the turtle and the pen color. We use alex.color("blue","red") to set the turtle to draw in blue,
# and fill in red.
#
# Ok, so can we get tess to draw a bar chart? Let us start with some data to be charted,
#
# xs = [48, 117, 200, 240, 160, 260, 220]
#
# Corresponding to each data measurement, well draw a simple rectangle of that height, with a fixed width.

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
    t.end_fill()             # Added this line
    t.forward(10)

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