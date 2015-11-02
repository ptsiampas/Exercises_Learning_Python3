# 5. Your traffic light controller program has been patented, and you’re about to become seriously rich. But your
# new client needs a change. They want four states in their state machine: Green, then Green and Orange together,
# then Orange only, and then Red. Additionally, they want different times spent in each state. The machine should
# spend 3 seconds in the Green state, followed by one second in the Green+Orange state, then one second in the
# Orange state, and then 2 seconds in the Red state. Change the logic in the state machine.
import turtle           # Tess becomes a traffic light.

# colours: green, darkgreen, orange, darkorange, red, darkred

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
# Inital States
red_off = "#731E1E"
orange_off = "#B9640F"
green_off = "#255025"
green_on = "#00FF00"
green = turtle.Turtle()
green.fillcolor(green_on)
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

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    # colours: green, darkgreen, orange, darkorange, red, darkred
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        green.fillcolor(green_on)    # on green
        red.fillcolor(red_off)    # off red
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:
        orange.fillcolor("orange")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2:     # Transition from state 1 to state 2
        orange.fillcolor("orange")
        green.fillcolor(green_off)
        state_num = 3
        wn.ontimer(advance_state_machine, 1000)
    else:                    # Transition from state 2 to state 0
        red.fillcolor("red")
        orange.fillcolor(orange_off)
        green.fillcolor(green_off)
        state_num = 0
        wn.ontimer(advance_state_machine, 2000)

advance_state_machine()

wn.listen()                      # Listen for events
wn.mainloop()