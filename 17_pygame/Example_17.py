import pygame
import time


def main():
    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use
    surface_sz = 480  # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("pic/ball.jpeg")

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)  # (x, y, width, height)
    some_color = (255, 0, 0)  # A color is a mix of (Red, Green, Blue)

    # Create a font for rendering text
    my_font = pygame.font.SysFont('Courier', 16)

    # start settings for frame rate count.
    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:
        ev = pygame.event.poll()  # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # ... leave game loop

        # Update your game objects and data structures here...

        # do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1 - t0)
            t0 = t1

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # Copy our image to the surface, at this (x,y) posn
        main_surface.blit(ball, (100, 50))

        # Make a new surface with an image of the text
        the_text = my_font.render('Frame = {0}, rate = {1:.2f} fps'
                                  .format(frame_count, frame_rate), True, (0, 0, 0))

        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()  # Once we leave the loop, close the window.


main()
