# Search Google for “sprite sheet playing cards”. Create a list [0..51] to represent an encoding
# of the 52 cards in a deck. Shuffle the cards, slice off the top five as your hand in
# a poker deal. Display the hand you have been dealt.
import pygame
import random


class Card_Sprite:
    def __init__(self, img):
        self.image = img
        self.target_pos = (0, 0)

    def update(self):
        return

    def darw(self, target_surface, position, card_id):
        self.target_pos = position
        x = 68 * card_id
        y = 0
        if 10 < card_id <= 20:
            x = 68 * (card_id % 10)
            y = 96

        size_x = 66
        size_y = 95
        target_surface.blit(self.image, self.target_pos, (x, y, size_x, size_y))

    def handle_click(self):
        return

    def contains_point(self):
        return


def draw_table(cards):
    pygame.init()
    bk_colour = (0, 125, 0)  # Colour of the table.
    surface_sz = (640, 480)
    surface = pygame.display.set_mode(surface_sz)

    # Card holders starting point
    card_size = (66, 95)
    card_start_loc = (50, 50)
    card_holder_colour = (255, 255, 0)

    # Build the deck
    full_deck_sheet = pygame.image.load("pic/CardDeck.png")
    card1 = Card_Sprite(full_deck_sheet)
    deck_of_cards = []

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            if key == 27:  # on Escape key
                break  # leave the game loop
        # Update Objects

        # Draw the basic board.
        surface.fill(bk_colour)

        (x_location, y_location) = card_start_loc
        for x in cards:
            surface.fill(card_holder_colour, (x_location, y_location, card_size[0], card_size[1]))
            card1.darw(surface, (x_location, 50), x)
            x_location += card_size[0] + 15

        # Flip the surface
        pygame.display.flip()

    pygame.quit()


draw_table([0, 10, 11, 20])
