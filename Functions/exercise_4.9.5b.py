import turtle

def draw_line(t, w):
    """
    :param t: turtle object to move
    :param w: width of line
    """
    for i in range(2):
        t.forward(w)
        t.left(90)



turtle.setup(600,400)       # Set the size of the window to 600x400
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Exercise 4.9.4")

alex=turtle.Turtle()
alex.pensize(2)
alex.color("blue")

ln=5

for i in range(50):
    draw_line(alex,ln+(i*5))
    alex.left(2)


turtle.mainloop()

