import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("hotpink")
tess.shape("square")

alex = turtle.Turtle()       # Create alex
alex.shape("turtle")         # Assin the turtle shape
alex.penup()
alex.forward(200)
alex.pendown()

for i in range(3):           # Make tess draw equilateral triangle
    tess.pensize(i+2)
    tess.forward(80)
    tess.left(120)

tess.penup()
tess.right(180)              # Turn tess around
tess.forward(80)             # Move her away from the origin
tess.pendown()

#for i in [0,1,2,3]:           # Make alex draw a square
#for i in range(4):           # Counting loop version 2
#for c in ["yellow", "red", "blue", "purple"]:
clrs = ["yellow", "red", "blue", "purple"]
for c in clrs:
    alex.color(c)
    alex.forward(50)
    alex.left(90)

turtle.mainloop()
