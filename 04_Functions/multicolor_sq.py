import turtle
__import__("turtle").__tracable__ = False

def draw_multicolor_square(t, sz):
    """
    Make turtle t draw multi-clor square of sz.
    """
    for i in ["red","purple","hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

turtle.setup(600,400)       # Set the size of the window to 600x400
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(tess,size)
    size += 10
    tess.forward(10)
    tess.right(18)
    
turtle.mainloop()