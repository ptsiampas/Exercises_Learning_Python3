__author__ = 'petert'
import turtle
import math

def draw_rectangle(t, w, h):
    """
    :param t: turtle object to move
    :param w: width of rectangle
    :param h: height of rectable
    :return: none
    """
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx,sz):
    """Make turtle t draw a square of sz."""
    draw_rectangle(tx,sz,sz)

def move_me(tx):
    tx.penup()
    tx.right(135)
    tx.forward(anglmv)
    tx.pendown()
    tx.left(135)


turtle.setup(600,400)       # Set the size of the window to 600x400
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets function")

alex=turtle.Turtle()
alex.pensize(3)
size=10
anglmv=math.hypot(size,size)
step=1

for i in range(10):
    draw_square(alex,size*step)
    move_me(alex)
    step+=2

turtle.mainloop()