# TickOatsTwoTest
This project is a test to see if the new version of TickTacToe made by Oats Jenkins (https://www.youtube.com/watch?v=ePxrVU4M9uA&amp;t=313s) has a winning strategy for either of the players.

The python file contains a function named recursive. It takes in a certain set of previous actions and returns what the outcome of the game will be if both players play optimally. So this can either be that player 1 wins (3), there is a draw (2) or player 2 wins (1).
The way the previous turns are encoded is by giving each tile of the playing board a number. Where,
- 1 is the upperleft tile
- 2 is the uppermid tile
- 3 is the upperright tile
- 4 is the midleft tile
- 5 is the middle tile
- 6 is the midright tile
- 7 is the lowerleft tile
- 8 is the lowermid tile
- 9 is the lowerright tile
This way
