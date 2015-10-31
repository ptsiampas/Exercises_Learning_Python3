# You and your friend are in a team to write a two-player game, human against computer, such as Tic-Tac-Toe / Noughts
# and Crosses. Your friend will write the logic to play one round of the game, while you will write the logic to allow
# many rounds of play, keep score, decide who plays, first, etc. The two of you negotiate on how the two parts of the
# program will fit together, and you come up with this simple scaffolding (which your friend will improve later):
#
# a. Write the main program which repeatedly calls this function to play the game, and after each round it announces
#    the outcome as “I win!”, “You win!”, or “Game drawn!”. It then asks the player “Do you want to play again?” and
#    either plays again, or says “Goodbye”, and terminates.
#
# b. Keep score of how many wins each player has had, and how many draws there have been. After each round of play,
#    also announce the scores.
#
# c. Add logic so that the players take turns to play first.
#
# d. Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each
#    round.
#
# e. Draw a flowchart of your logic.

# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result


def calc_percentage(pscore, cscore):
    # d. Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each
    #    round.
    # Avoid the evil divide by 0 error.
    if pscore >= 1 and cscore == 0:
        return pscore * 100
    elif cscore == 0 or pscore == 0:
        return 0

    # First: work out the difference (decrease) between the two numbers you are comparing.
    decrese = pscore - cscore

    # Then: divide the decrease by the original number and multiply the answer by 100.
    pdecrese = decrese / pscore * 100
    return pdecrese

# a. Write the main program which repeatedly calls this function to play the game, and after each round it announces
#    the outcome as “I win!”, “You win!”, or “Game drawn!”. It then asks the player “Do you want to play again?” and
#    either plays again, or says “Goodbye”, and terminates.
again="y"
ptally=0
ctally=0
ntally=0
last_played=1

while again != "n":
    # c. Add logic so that the players take turns to play first.
    if last_played == 1:
        game_result=play_once(False)
        last_played = 0
    else:
        game_result=play_once(True)
        last_played = 1

    # b. Keep score of how many wins each player has had, and how many draws there have been. After each round of play,
    #    also announce the scores.
    if game_result == -1:
        print("You Win!",end=": ")
        ptally+=1
    elif game_result == 1:
        print("I Win!",end=": ")
        ctally+=1
    else:
        print("Game Drawn!",end=": ")
        ntally+=1
    print("Tally: Me({0}), You({1})[{3:.2f}%], Drawn({2})\n"
          .format(ctally,ptally,ntally,calc_percentage(ptally,ctally)))

    again = input("Do you want to play again (n to quit)? ")

# d. Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each
#    round.
print("Final Tally: Me({0}), You({1})[{3:.2f}%], Drawn({2})\n"
          .format(ctally,ptally,ntally,calc_percentage(ptally,ctally)))
print("Goodbye!")