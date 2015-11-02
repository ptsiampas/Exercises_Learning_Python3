# 1. Add some new key bindings to the first sample program:
#
#  - Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
#  - Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays
#    between 1 and 20 (inclusive).
#  - Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new
#    behaviour that can be controlled from the keyboard.
import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)


def h2():
   tess.left(45)


def h3():
   tess.right(45)


def h4():
    wn.bye()                        # Close down the turtle window


def change_pen_color_red():
    """  - Pressing keys R, G or B should change tess’ color to Red, Green or Blue. """
    tess.color("Red")

def change_pen_color_green():
    """  - Pressing keys R, G or B should change tess’ color to Red, Green or Blue. """
    tess.color("Green")

def change_pen_color_blue():
    """  - Pressing keys R, G or B should change tess’ color to Red, Green or Blue. """
    tess.color("Blue")

def pen_size_up():
    """Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays"""
    global current_pen_size

    if current_pen_size == 20:
        current_pen_size = 1
    else:
        current_pen_size += 1

    wn.title("Pen Size {0}".format(current_pen_size))
    tess.pensize(current_pen_size)


def pen_size_down():
    """Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays"""
    global current_pen_size

    if current_pen_size == 1:
        current_pen_size = 20
    else:
        current_pen_size -= 1

    wn.title("Pen Size {0}".format(current_pen_size))
    tess.pensize(current_pen_size)

def pen_up():
    """
    don't draw
    :return: None
    """
    tess.penup()

def pen_down():
    """
    Star Drawing
    :return:
    """
    tess.pendown()

current_pen_size = 1
# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

#  - Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
wn.onkey(change_pen_color_red, "r")
wn.onkey(change_pen_color_green, "g")
wn.onkey(change_pen_color_blue, "b")

#  - Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays
#    between 1 and 20 (inclusive).
wn.onkey(pen_size_up, "plus")
wn.onkey(pen_size_up, "equal")      # because who wants to hold down shift.
wn.onkey(pen_size_down, "minus")

#  - Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new
#    behaviour that can be controlled from the keyboard.
wn.onkey(pen_up, "Prior")
wn.onkey(pen_down, 'Next')

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
