import turtle

wn = turtle.Screen()
wn.title("Example 18.1 Drawing Fractals!")
wn.bgcolor("white")
fract_turtle = turtle.Turtle()
fract_turtle.pencolor("#0000FF")
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
        for angle in [-60, 120, -60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


def draw_poly(turtle, sides, line_length):
    for i in range(sides):
        # turtle.forward(line_length)
        koch(turtle, 3, line_length)
        turtle.left(360 / sides)


draw_poly(fract_turtle, 4, 100)

# koch(fract_turtle, 2, 100)

wn.mainloop()
