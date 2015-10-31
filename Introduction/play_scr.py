import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")  # Sets window background colour
wn.title("Hey its me")    # Sets title


alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.color("blue")        # pen colour blue
alex.pensize(3)           # Set pen size
alex.forward(50)          # Tell alex to move forward by 50 units
alex.left(120)             # Tell alex to turn by 90 degrees
alex.forward(50)          # Complete the second side of a rectangle

turtle.mainloop()             # Wait for user to close window