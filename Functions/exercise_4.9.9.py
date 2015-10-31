#  Write a void function to draw a star, where the length of each side is 100 units.
#  (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle

def draw_pentagram(t,sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

pent=turtle.Turtle()
pent.color("hotpink")
pent.pensize(3)

draw_pentagram(pent,100)

turtle.mainloop()
