# 3. In an earlier chapter we saw two turtle methods, hideturtle and showturtle that can hide or show a turtle.
# This suggests that we could take a different approach to the traffic lights program. Modify the program so that
# we create three separate turtles for each of the green, orange and red lights, and instead of moving tess to
# different positions and changing her color, we just make one of the three turtles visible at any time. Once you’ve
# made the changes, sit back and ponder some deep thoughts: you’ve got two programs, both seem to do the same thing.
# Is one approach somehow preferable to the other? This approach, since it flicks between the actual lights, like real
# ones.
# Which one more closely resembles reality
# i.e. the traffic lights in your town?

import turtle           # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
green = turtle.Turtle()
green.fillcolor("green")
red = turtle.Turtle()
red.fillcolor("red")
yellow = turtle.Turtle()
yellow.fillcolor("yellow")
border = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    border.hideturtle()
    border.pensize(3)
    border.color("black", "darkgrey")
    border.begin_fill()
    border.forward(80)
    border.left(90)
    border.forward(200)
    border.circle(40, 180)
    border.forward(200)
    border.left(90)
    border.end_fill()


def setup_lights(turt_data):
    (turt, location) = turt_data

    if turt.color() == "green":
        turt.showturtle()
    turt.hideturtle()
    turt.penup()
    turt.forward(40)
    turt.left(90)
    turt.forward(location)
    turt.shape("circle")
    turt.shapesize(3)


lights = [
    (red, 200),
    (yellow, 130),
    (green, 50)
]

draw_housing()
for x in range(len(lights)):
    setup_lights(lights[x])

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        green.showturtle()
        red.hideturtle()
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:     # Transition from state 1 to state 2
        yellow.showturtle()
        green.hideturtle()
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    else:                    # Transition from state 2 to state 0
        red.showturtle()
        yellow.hideturtle()
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

advance_state_machine()

wn.listen()                      # Listen for events
wn.mainloop()