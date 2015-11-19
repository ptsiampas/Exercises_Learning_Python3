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

    def draw(self, target_surface, position, sprite_location):
        self.target_pos = position
        (sprite_loc_x, sprite_y) = sprite_location
        target_surface.blit(self.image, self.target_pos, (sprite_loc_x, sprite_y, 66, 95))

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
    card_start_loc = (10, 50)
    card_holder_colour = (255, 255, 0)

    # Build the deck
    full_deck_sheet = pygame.image.load("pic/CardDeck.png")

    card_sprites = Card_Sprite(full_deck_sheet)

    deck_of_cards = []
    for ly in range(0, 480, 96):
        for lx in range(0, 748, 68):
            deck_of_cards.append((lx, ly))
            if len(deck_of_cards) >= 51:
                break

    # Shuffle the cards
    rng = random.Random()
    rng.shuffle(deck_of_cards)
    cards = deck_of_cards[:5]

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
        for the_card in cards:
            surface.fill(card_holder_colour, (x_location, y_location, card_size[0], card_size[1]))
            card_sprites.draw(surface, (x_location, y_location), the_card)
            x_location += card_size[0] + 10

        # Flip the surface
        pygame.display.flip()

    pygame.quit()


items = []
for x in range(15, 20):
    items.append(x)
draw_table(items)
