import turtle

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes

# setup each starting point.

triangle=turtle.Turtle()
triangle.color("green")
triangle.penup()
triangle.forward(200)
triangle.pendown()

square=turtle.Turtle()
square.color("blue")
square.penup()
square.forward(50)
square.pendown()

hexagon=turtle.Turtle()
hexagon.color("red")
hexagon.penup()
hexagon.forward(-50)
hexagon.pendown()

octagon=turtle.Turtle()
octagon.color("purple")
octagon.penup()
octagon.forward(-200)
octagon.pendown()


# An equilateral triangle
for i in range(3):
    triangle.forward(80)
    triangle.left(120)

for i in range(4):
    square.forward(80)
    square.left(90)

for i in range(6):
    hexagon.forward(60)
    hexagon.left(60)

for i in range(8):
    octagon.forward(40)
    octagon.left(45)

turtle.mainloop()