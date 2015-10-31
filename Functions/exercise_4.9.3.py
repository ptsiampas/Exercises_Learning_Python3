import turtle
import math

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

turtle.setup(600,400)       # Set the size of the window to 600x400
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

draw_poly(tess,8, 50)

turtle.mainloop()
