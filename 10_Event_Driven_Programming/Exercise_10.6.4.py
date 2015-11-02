# 5. Now that you’ve got a traffic light program with different turtles for each light, perhaps the
# visibility / invisibility trick wasn’t such a great idea. If we watch the traffic lights, they turn on and off
# but when they’re off they are still there, perhaps just a darker color. Modify the program now so that the lights
# don’t disappear: they are either on, or off. But when they’re off, they’re still visible
import turtle           # Tess becomes a traffic light.

# colours: green, darkgreen, orange, darkorange, red, darkred

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
# Inital States
green = turtle.Turtle()
green.fillcolor("green")
red = turtle.Turtle()
red.fillcolor("darkred")
orange = turtle.Turtle()
orange.fillcolor("darkorange")
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

    turt.penup()
    turt.forward(40)
    turt.left(90)
    turt.forward(location)
    turt.shape("circle")
    turt.shapesize(3)


lights = [
    (red, 200),
    (orange, 130),
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
    # colours: green, darkgreen, orange, darkorange, red, darkred
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        green.fillcolor("green")    # on green
        red.fillcolor("darkred")    # off red
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:     # Transition from state 1 to state 2
        orange.fillcolor("orange")
        green.fillcolor("darkgreen")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    else:                    # Transition from state 2 to state 0
        red.fillcolor("red")
        orange.fillcolor("darkorange")
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

advance_state_machine()

wn.listen()                      # Listen for events
wn.mainloop()