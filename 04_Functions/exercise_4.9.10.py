# Extend your program from Ex 4.9.9. Draw five stars, but between each, pick up the pen,
# move forward by 350 units, turn right by 144, put the pen down, and draw the next star.
# Youll get something like this:

import turtle

def draw_pentagram(t,sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Exercise 4.9.10")

pent=turtle.Turtle()
pent.color("hotpink")
pent.pensize(3)

for i in range(5):
    draw_pentagram(pent,100)
    pent.penup()
    pent.forward(350)
    pent.right(144)
    pent.pendown()

turtle.mainloop()