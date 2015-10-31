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
wn.title("Exercise 4.9.4")

alex=turtle.Turtle()
alex.pensize(2)
alex.color("blue")

size=100
for i in range(20):         # I am sure this could be written better..
    draw_square(alex,size)
    alex.right(20)

turtle.mainloop()