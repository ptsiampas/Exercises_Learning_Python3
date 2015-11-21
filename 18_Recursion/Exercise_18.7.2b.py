from turtle import *


def cesaro_fractal(turtle, order, length):
    """
    (a) Draw a Casaro torn line fractal, of the order given by the user.
    We show four different lines of order 0, 1, 2, 3. In this example, the angle of the
    tear is 10 degrees.
    :return:
    """
    if order == 0:  # The base case is just a straight line
        turtle.forward(length)
    else:
        for angle in [-85, 170, -85, 0]:
            cesaro_fractal(turtle, order - 1, length / 2)
            turtle.left(angle)


wn = Screen()
wn.title("Exercise 18.7.2a Cesaro Fractal!")
wn.bgcolor("white")
fract_turtle = Turtle()
fract_turtle.pencolor("#0000FF")
fract_turtle.pensize(1)

# setup initial location
delay(0)
fract_turtle.speed(0)
fract_turtle.up()
fract_turtle.goto(-450, 300)
fract_turtle.down()
fract_turtle.pendown()
fract_turtle.hideturtle()
size = 150
sides = 4

for order in [0, 1, 2, 3]:
    for i in range(sides):
        cesaro_fractal(fract_turtle, order, size)
        fract_turtle.right(360 / sides)

    fract_turtle.penup()
    fract_turtle.forward(size + 50)
    fract_turtle.pendown()

exitonclick()
