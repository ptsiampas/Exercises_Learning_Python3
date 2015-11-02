__author__ = 'petert'
import turtle

turtle.setup(600,400)
wn = turtle.Screen()         # Set up the window and its attributes

dg=turtle.Turtle()

for tu in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    dg.forward(100)
    dg.left(tu)

turtle.mainloop()
