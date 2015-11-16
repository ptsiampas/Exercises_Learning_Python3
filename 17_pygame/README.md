# Chapter 17 PyGame
Source: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/pygame.html

## Exercises

1. Have fun with Python, and with PyGame. **Always**
2. **[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/17_pygame/Example_17.6.py)** We deliberately left a bug in the code for animating Duke. If you click on one of the chessboard squares to the right of Duke, he waves anyway. Why? Find a one-line fix for the bug.
   **Line 79 had the width of the entire image, so from its position it had a width of 500, changed it to 50 to restrict its view.**
3. **[current](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/17_pygame/Example_17.10.3.py)** Use your preferred search engine to search their image library for “sprite sheet playing cards”. Create a list [0..51] to represent an encoding of the 52 cards in a deck. Shuffle the cards, slice off the top five as your hand in a poker deal. Display the hand you have been dealt.
4. So the Aliens game is in outer space, without gravity. Shots fly away forever, and bombs don’t speed up when they fall. Add some gravity to the game. Decide if you’re going to allow your own shots to fall back on your head and kill you.
5. Those pesky Aliens seem to pass right through each other! Change the game so that they collide, and destroy each other in a mighty explosion.
