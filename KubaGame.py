# Author: Jonathan Luong
# Date: 5/31/21
# Description: A program clone of Kuba, the board game


class KubaGame:
    """
    This class is our overall game class.
    Contains all methods for initializing the game and various moves/options a player has.
    Takes as its parameters two tuples and will work the GameBoard, Player, and Marble objects.
    """

    def __init__(self, p1: tuple, p2: tuple):
        """
        initializes the Player, GameBoard, and Marble objects of the game
        :param p1: player name and color of the marble ('PlayerA', 'B')
        :param p2: player name and color of the marble ('PlayerB', 'W')
        """
        # self.p1_name = p1[0]
        # self.p2_name = p2[0]
        # self.p1_color = p1[1]
        # self.p2_color = p2[1]
        self.p1 = Player(p1[0], p1[1])
        self.p2 = Player(p1[0], p1[1])
        self.board = self.create_board()
        self.current_player_turn = None

    def create_board(self):
        r0 = ['W', 'W', 'X', 'X', 'X', 'B', 'B']
        r1 = ['W', 'W', 'X', 'R', 'X', 'B', 'B']
        r2= ['X', 'X', 'R', 'R', 'R', 'X', 'X']
        r3 = ['X', 'R', 'R', 'R', 'R', 'R', 'X']
        r4 = r2.copy()
        r5 = r1.copy()
        r5.reverse()
        r6 = r0.copy()
        r6.reverse()
        return [r0, r1, r2, r3, r4, r5, r6]



    def display_board(self):
        """
        Methods to get a visual of the board
        :return: a visual print of the board in console
        """
        for row in self.board:
            print(row)


    def get_current_turn(self):
        """
        Will determine whose turn it currently is. Will work with Player class methods.
        :return: Player name
        """
        return self.current_player_turn


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
        white_m = 0
        black_m = 0
        red_m = 0
        for row in self.board:
            for square in row:
                if square == 'W':
                    white_m += 1
                elif square == 'B':
                    black_m += 1
                elif square == 'R':
                    red_m += 1
        tup_marbles = (white_m, black_m, red_m)
        return tup_marbles

        # white_m = {k: v for k,v in self.board.items() if v == 'W'}
        # black_m = {k: v for k, v in self.board.items() if v == 'B'}
        # red_m = {k: v for k, v in self.board.items() if v == 'R'}
        # tup_marbles = (len(white_m), len(black_m), len(red_m))
        # return tup_marbles

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
        self.name = name
        self.color = color

    def player_marbles(self):
        # if self.color =
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
        self.color = None

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

class White(Marble):

    def __init__(self):
        self.color = 'W'


class Black(Marble):

    def __init__(self):
        self.color = 'B'


class Red(Marble):

    def __init__(self):
        self.color = 'R'

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


whitemarble = {'W': White(), 'W': White()}
game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
game.create_board()
game.display_board()
print(game.get_marble_count())
# print(whitemarble)

# def create_board(self):
#     squares = []
#     column = 0
#     row = 0
#     while column < 7:
#         while row < 7:
#             squares.append((column, row))
#             row += 1
#         column += 1
#         row = 0
#
#     for (x, y) in squares:
#         if x < 2 and y < 2:
#             self.board.update({(x, y): {'W': White()}})
#         elif x > 4 and y > 4:
#             self.board.update({(x, y): {'W': White()}})
#         elif x > 4 and y < 2:
#             self.board.update({(x, y): {'B': Black()}})
#         elif x < 2 and y > 4:
#             self.board.update({(x, y): {'B': Black()}})
#         elif x == 3 and (y == 1 or y == 5):
#             self.board.update({(x, y): {'R': Red()}})
#         elif (y == 2 or y == 4) and 1 < x < 5:
#             self.board.update({(x, y): {'R': Red()}})
#         elif y == 3 and 0 < x < 6:
#             self.board.update({(x, y): {'R': Red()}})
#         else:
#             self.board.update({(x, y): {'X': None}})