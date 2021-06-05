# Author: Jonathan Luong
# Date: 5/31/21
# Description: A program clone of Kuba, the board game


class KubaGame:
    """
    This class is our overall game class.
    Contains all methods for initializing the game and various moves/options a player has.
    Takes as its parameters two tuples and will work the GameBoard, Player, and Marble objects.
    """
    def __init__(self, p1, p2):
        """
        initializes the Player, GameBoard, and Marble objects of the game
        :param p1: player name and color of the marble ('PlayerA', 'B')
        :param p2: player name and color of the marble ('PlayerB', 'W')
        """
        pass

    def get_current_turn(self):
        """
        Will determine whose turn it currently is. Will work with Player class methods.
        :return: Player name
        """
        pass

    def make_move(self, playername, coordinates, direction):
        """
        Method to initiate a move. Will work with Marble and GameBoard classes to determine validity and
        :param playername: Player making the move
        :param coordinates: Coordinates of marble to move
        :param direction: One of the 4 directions to move
        :return: Either updated board with move, or will state invalid move and show the board again.
        """
        pass

    def get_winner(self):
        """
        method to determine if there is a winner or not when called. Will work with Player class methods.
        :return: Player name or None
        """
        pass

    def get_captured(self, playername):
        """
        Method  to determine how many red marbles a player has captured. Will work with GameBoard class methods.
        :param playername: Player name
        :return: Count of red marbles that player has captured
        """
        pass

    def get_marble(self, coord):
        """
        Method to determine what color marble (if any) is at a given coordinate
        :param coord:
        :return: Marble color found at square or 'X'
        """
        pass

    def get_marble_count(self):
        """
        Method to determine the number of marbles on the board. Will work with GameBoard class Methods
        :return: Tuple of White marbles, Black marbles and Red marbles (W,B,R)
        """
        pass


class GameBoard:
    """
    Class for the game board object. Will contain code for visualizing the board and any methods for changing/updating this.

    """
    def __init__(self):
        """
        Initializes properties for the game board.
        """
        pass

    def create_board(self):
        board_squares = {(1,1): 'X'}

    def get_board(self):
        """
        Methods to get a visual of the board
        :return: a visual print of the board in console
        """
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')
        print('|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|'+'X'+'|')
        print('--+-+-+-+-+-+--')



class Player:
    """
    Class for player object and various methods related to them.
    Will record the player information and keep track of whose turn it is
    """
    def __init__(self, name, color):
        """
        Will initialize the properties of a player
        :param name: Player Name
        :param color: Color of Marbles
        """
        pass

    def get_turn_player(self):
        """
        Method to get the current turns player
        :return: player name
        """
        pass

    def set_turn_player(self, player):
        """
        Method to set the current turns player
        :param player: player name
        :return: player name
        """
        pass

    def get_game_winner(self):
        """
        Method to get the games winner
        :return: player name
        """
        pass

    def set_game_winner(self, player):
        """
        Method to set the games winner
        :param player: player name
        :return: player name
        """
        pass

class Marble:
    """
    Class for marble object of the board game.
    Controls whether or not a marble can move in a given direction
    """
    def __init__(self):
        pass

    def backward(self):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        pass

    def left(self):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        pass

    def right(self):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        pass

    def forward(self):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        pass

class Queue:
    """
    An implementation of the Queue ADT that uses Python's built-in lists
    Debating on whether to use this for moving marbles on the board....
    """

    def __init__(self):
        self.list = []

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        val = self.list[0]
        del self.list[0]
        return val

    def is_empty(self):
        return len(self.list) == 0

kubaboard = GameBoard()
kubaboard.get_board()