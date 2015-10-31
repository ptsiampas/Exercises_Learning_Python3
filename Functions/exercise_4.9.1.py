__author__ = 'petert'
import turtle

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

turtle.setup(600,400)       # Set the size of the window to 600x400
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets function")

alex=turtle.Turtle()
alex.pensize(3)

size=20
for i in range(5):
    draw_square(alex,size)
    alex.penup()
    alex.forward(size+size)
    alex.pendown()

turtle.mainloop()