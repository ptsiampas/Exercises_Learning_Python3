from turtle import *


def Triangle(t, length):
    for angle in [120, 120, 120]:
        t.forward(length)
        t.left(angle)


def sierpinski_triangle(turtle, order, length):
    """
    3. A Sierpinski triangle of order 0 is an equilateral triangle. An order 1 triangle can be drawn by drawing 3
    smaller triangles (shown slightly disconnected here, just to help our understanding).
    Higher order 2 and 3 triangles are also shown.
    Draw Sierpinski triangles of any order input by the user..
    :return:
    """
    if order == 0:  # The base case is just a straight line
        Triangle(turtle, length)
    else:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
            sierpinski_triangle(turtle, order - 1, length / 2)


wn = Screen()
wn.title("Exercise 18.7.3 Sierpinski triangle Fractal!")
wn.bgcolor("white")
fract_turtle = Turtle()
fract_turtle.pencolor("#0000FF")
fract_turtle.fillcolor("black")
fract_turtle.pensize(1)

# setup initial location
# delay(0)
fract_turtle.speed(0)
fract_turtle.up()
fract_turtle.goto(-450, -200)
fract_turtle.down()
fract_turtle.pendown()
fract_turtle.hideturtle()
size = 200

sierpinski_triangle(fract_turtle, 4, size)

exitonclick()
