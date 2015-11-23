# Levy Dragon Fractal Curve
# FB - 200912093

from turtle import *


def draw_fractal(length, angle, level, initial_state, target, replacement, target2, replacement2):
    state = initial_state

    for counter in range(level):
        state2 = ''
        for character in state:
            if character == target:
                state2 += replacement
            elif character == target2:
                state2 += replacement2
            else:
                state2 += character
        state = state2

    # draw
    for character in state:
        if character == 'F':
            forward(length)
        elif character == '+':
            right(angle)
        elif character == '-':
            left(angle)


if __name__ == '__main__':
    delay(0)
    speed(0)
    up()
    goto(-180, 60)
    down()
    draw_fractal(5, 90, 10, 'FX', 'X', 'X+YF+', 'Y', '-FX-Y')
    # draw_fractal(1, 60, 5, 'X++X++X', 'X', 'FX-FX++XF-XF', '', '')
    # draw_fractal(2, 75, 6, 'FX', 'X', 'X-FX++FX-FX', '', '')
    # draw_fractal(2, 45, 10, 'F', 'F', '+F--F+', '', '')
    exitonclick()
