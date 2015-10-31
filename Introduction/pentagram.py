__author__ = 'petert'
import turtle

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes

pent=turtle.Turtle()
pent.hideturtle()

for i in range(5):
    pent.forward(100)
    pent.right(144)


turtle.mainloop()