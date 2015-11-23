from turtle import *


def Triangle(t, length):
    for angle in [120, 120, 120]:
        t.forward(length)
        t.left(angle)


def moveToNextPosision(turtle, length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()
    turtle.left(120)


def sierpinski_triangle(turtle, order, length, colorChangeDepth=-1):
    """
    4. Adapt program from exercise 18.7.3  to change the color of its three sub-triangles at some depth
      of recursion. The illustration below shows two cases: on the left, the color is changed
      at depth 0 (the outmost level of recursion), on the right, at depth 2. If the user supplies
      a negative depth, the color never changes.
      (Hint: add a new optional parameter colorChangeDepth (which defaults to -1), and make this one smaller on each
      recursive subcall. Then, in the section of code before you recurse, test whether the parameter is zero,
      and change color.)
    :return:
    """
    if order == 0:  # The base case is just a straight line
        print("Order 0")
        Triangle(turtle, length)
    else:
        print("First call", colorChangeDepth)
        moveToNextPosision(turtle, length)
        if colorChangeDepth == 0:
            turtle.pencolor("blue")
        sierpinski_triangle(turtle, order - 1, length / 2, colorChangeDepth - 1)

        print("Second call", colorChangeDepth)
        moveToNextPosision(turtle, length)
        if colorChangeDepth == 0:
            turtle.pencolor("magenta")
        sierpinski_triangle(turtle, order - 1, length / 2, colorChangeDepth - 1)

        print("Third call", colorChangeDepth)
        moveToNextPosision(turtle, length)
        if colorChangeDepth == 0:
            turtle.pencolor("red")
        sierpinski_triangle(turtle, order - 1, length / 2, colorChangeDepth - 1)


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
size = 400

sierpinski_triangle(fract_turtle, 4, size, 0)

exitonclick()
