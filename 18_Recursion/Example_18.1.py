import turtle

wn = turtle.Screen()
wn.title("Example 18.1 Drawing Fractals!")
wn.bgcolor("white")
fract_turtle = turtle.Turtle()
fract_turtle.pencolor("#FF0000")
fract_turtle.hideturtle()
fract_turtle.pensize(2)


def koch(t, order, size):
    """
    Make turtle t draw a Koch fractal of ’order’ and ’size’.
    Leave the turtle facing the same direction.
    """
    if order == 0:  # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)
            # koch(t, order - 1, size / 3)  # go 1/3 of the way
            # t.left(60)
            # koch(t, order - 1, size / 3)
            # t.right(120)
            # koch(t, order - 1, size / 3)
            # t.left(60)
            # koch(t, order - 1, size / 3)


koch(fract_turtle, 4, 400)

wn.mainloop()
