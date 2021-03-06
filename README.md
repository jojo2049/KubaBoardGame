# KubaBoardGame

The goal of this class project was to create Kuba boardgame clone. Rules on how to play Kuba can be found [here](https://sites.google.com/site/boardandpieces/list-of-games/kuba). You can also watch
this youtube video that shows how the game is played [here](https://www.youtube.com/watch?v=XglqkfzsXYc). Below are some general guidelines for the game:

Game ends when a player wins. A players wins by pushing off and capturing seven neutral red stones or by pushing off all of the opposing stones. A player who has no legal moves available has lost the game.

Any player can start the game.

The initial setup of the board will be as shown in the figure in the kuba game rules website. 

Rules to move a marble:
- You need an empty space(or the edge of the board) on the side you are pushing away from. This is as shown in the video.
- A player cannot undo a move the opponent just made (if it leads to the exact same board position)

Below are some of the criteria we had to meet for the project:

Your KubaGame class **must** include the following:

* An `init` method that takes as its parameters two tuples, each containing player name and color of the marble that the player is playing (ex: ('PlayerA', 'B'), ('PlayerB','W')) and it initializes the board. On the board R, B, W can be used to represent Red, Black and White marbles. 

* A method called `get_current_turn` that returns the player name whose turn it is to play the game. It should return `None` if called when no player has made the first move yet, since any player can start the game.

* A method called `make_move` that takes three parameters `playername`, `coordinates` i.e. a tuple containing the location of marble that is being moved and the `direction` in which the player wants to push the marble. Valid directions are `L`(Left), `R`(Right), `F`(Forward) and `B`(Backward). The directions are explained using a diagram below.
  - If any opponent marble is pushed off it is removed from the board. 
  - If a Red marble is pushed off it is considered captured by the player who made the move. 
  - If the move is successful, this method should return `True`. 
  - If the move is being made after the game has been won, or when it's not the player's turn or if the coordinates provided are not valid, or a marble in the coordinates cannot be moved in the direction specified, or it is not the player's marble or for any other invalid conditions return `False`.  

* A method called `get_winner` that returns the name of the winning player. If no player has won yet, it returns `None`. Note that this does *not* return the color that the player chose.

* A method called `get_captured` that takes player's name as parameter and returns the number of Red marbles captured by the player. This returns 0 if no marble is captured.

* A method called `get_marble` that takes the coordinates of a cell as a tuple and returns the marble that is present at the location. If no marble is present at the coordinate location return 'X'.

* A method called `get_marble_count` that returns the number of White marbles, Black marbles and Red marbles as tuple in the order (W,B,R). This order is important.

The names of players will be decided by the user of your game and will always be passed in the same way as it is passed when initializing the KubaGame object. The marbles are always represented as upper case R, B, W in the method calls and your methods should use the same representation when returning any relevant values. Similarly, X, L, R, F and B that represent absence of marble and all the four directions respectively should also be in upper case.

**A note about the coordinates**: The top left cell on the board is referred to by (0,0),  and the bottom right cell by (6,6). i.e **(row_number, col_number)**