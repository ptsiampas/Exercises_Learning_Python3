import pygame

gravity = 0.01


class QueenSprite:
    def __init__(self, col, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board
        """
        self.image = img
        self.col_number = col
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)  # Start ball at top of its column
        self.y_velocity = 0  # with zero initial velocity

    def update(self):
        self.y_velocity += gravity  # Gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity  # Velocity moves the ball

        (target_x, target_y) = self.target_posn  # Unpack the position
        dist_to_go = target_y - new_y_pos  # How far to our floor?

        if dist_to_go < 0:  # Are we under floor?
            self.y_velocity = -0.65 * self.y_velocity  # Bounce
            new_y_pos = target_y + dist_to_go  # Move back above floor

        self.posn = (x, new_y_pos)  # to this new position.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

    def printxy(self):
        print("Queen[{2}] (x,y) & Target ():({0}), {1}".format(self.posn, self.target_posn, self.col_number))

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + my_width and
                y >= my_y and y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -0.3         # Kick it back up.

def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]  # Set up colors [red, black]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    surface_sz = n * sq_sz  # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    queen = pygame.transform.scale(pygame.image.load("pic/queen.png"),
                                   (int(sq_sz - 4), int(sq_sz - 4)))

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    queen_offset = (sq_sz - queen.get_width()) // 2

    all_sprites = []  # Keep track of all the sprites

    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(col, queen,
                              (col * sq_sz + queen_offset, row * sq_sz + queen_offset))
        all_sprites.append(a_queen)

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            if key == 27:  # On Escape key ...
                break  # leave the game loop.
            if key == ord('r'):
                colors[0] = (255, 0, 0)  # Change to red + black.
            elif key == ord('g'):
                colors[0] = (0, 255, 0)  # Change to green + black.
            elif key == ord('b'):
                colors[0] = (0, 0, 255)  # Change to blue + black.

        if ev.type == pygame.MOUSEBUTTONDOWN:  # Mouse gone down?
            posn_of_click = ev.dict['pos']  # Get the coordinates.
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

        for sprite in all_sprites:
            sprite.update()
            # sprite.printxy()

        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Alternate starting color
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Ask the sprite to draw its self
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])
