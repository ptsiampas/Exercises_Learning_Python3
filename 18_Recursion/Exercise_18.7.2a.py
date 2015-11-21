import turtle
from math import cos, sin


def cesaro_fractal(turtle, order, size):
    """
    (a) Draw a Casaro torn line fractal, of the order given by the user.
    We show four different lines of order 0, 1, 2, 3. In this example, the angle of the
    tear is 10 degrees.
    :return:
    """
    if order == 0:  # The base case is just a straight line
        turtle.forward(size)
    else:
        for angle in [-85, 170, -85, 0]:
            cesaro_fractal(turtle, order - 1, size / 3)
            turtle.left(angle)


wn = turtle.Screen()
wn.title("Exercise 18.7.2a Cesaro Fractal!")
wn.bgcolor("white")
fract_turtle = turtle.Turtle()
fract_turtle.pencolor("#0000FF")
fract_turtle.hideturtle()
fract_turtle.pensize(1)

# setup initial location
fract_turtle.penup()
fract_turtle.back(450)
fract_turtle.right(90)
fract_turtle.back(400)
fract_turtle.left(90)
fract_turtle.pendown()
size = 150

for order in [0, 1, 2, 3]:
    cesaro_fractal(fract_turtle, order, size + (50 * (order + 1)))
    fract_turtle.penup()
    fract_turtle.forward(50)
    fract_turtle.pendown()

wn.mainloop()
