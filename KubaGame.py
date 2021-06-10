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
        self.p1 = Player(p1[0], p1[1])
        self.p2 = Player(p2[0], p2[1])
        self.board = self.create_board()
        self.current_player = None

    def create_board(self):
        r0 = ['W', 'W', 'X', 'X', 'X', 'B', 'B']
        r1 = ['W', 'W', 'X', 'R', 'X', 'B', 'B']
        r2 = ['X', 'X', 'R', 'R', 'R', 'X', 'X']
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


    def get_current_player_name(self):
        """
        Will determine whose turn it currently is. Will work with Player class methods.
        :return: Player name
        """
        if self.current_player is None:
            return self.current_player
        else:
            return self.current_player.get_player_name()

    def set_current_player(self, player):
        """
        Method to set the current turns player
        :param player: player name
        :return: player name
        """
        self.current_player = player

    def change_current_player(self):
        """
        Method to swap current player
        """
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1


    def make_move(self, playername, coordinate, direction):
        """
        Method to initiate a move. Will work with Marble and GameBoard classes to determine validity and
        :param playername: Player making the move
        :param coordinate: Coordinates of marble to move
        :param direction: One of the 4 directions to move
        :return: Either updated board with move, or will state invalid move and show the board again.
        """

        if self.current_player is None:
            if playername == self.p1.get_player_name():
                self. set_current_player(self.p1)
            else:
                self.set_current_player(self.p2)

        if playername == self.current_player.get_player_name() and self.current_player.get_player_color() == self.get_marble(coordinate):
            if direction == 'L':
                pass
            elif direction == 'R':
                return self.move_right(coordinate)
            elif direction == 'F':
                return self.move_forward(coordinate)
            elif direction == 'B':
                return self.move_backward(coordinate)

            if playername == self.p1.get_player_name():
                self.set_current_player(self.p2)
                print('p2change')
                return True
            else:
                self.set_current_player(self.p1)
                print('p1change')
                return True
        else:
            return False


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
        if playername == self.p1.get_player_name():
            return self.p1.captured
        else:
            return self.p2.captured

    def get_marble(self, coordinate):
        """
        Method to determine what color marble (if any) is at a given coordinate
        :param coordinate provided as tuple
        :return: Marble color found at square or 'X'
        """
        row = coordinate[0]
        column = coordinate[1]
        return self.board[row][column]

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

    def set_game_winner(self, player):
        """
        Method to set the games winner
        :param player: player name
        :return: player name
        """
        pass

    def get_current_player(self):
        return self.current_player

    def move_backward(self, coordinate):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """

        column = coordinate[1]
        row = coordinate[0]
        column_squares = []
        temp = None
        for list in self.board:
            column_squares.append(list[column])

        if row == 0 and 'X' not in column_squares:
            temp = column_squares.pop()
            column_squares.insert(0, 'X')

        elif (row != 6 and column_squares[row-1] == 'X') or (row == 0 and 'X' in column_squares):
            location = row
            if 'X' in column_squares[row:]:
                for item in column_squares[row:]:
                    if item == 'X':
                        column_squares.pop(location)
                        column_squares.insert(row, 'X')
                        break
                    location += 1
            else:
                column_squares.insert(row, 'X')
                temp = column_squares.pop()


        elif row != 6 and column_squares[row-1] != 'X':
            return False

        tracker = 0
        for square in column_squares:
            self.board[tracker][column] = square
            tracker += 1

        if temp == 'R':
            self.get_current_player().update_captured()
            self.change_current_player()
        else:
            self.change_current_player()

        return True




    def move_left(self):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        pass

    def move_right(self, coordinate):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        row = coordinate[0]
        column = coordinate[1]

        if column == 0 and 'X' in self.board[row] is False:
            temp = self.board[row].pop()
            self.board[row].insert(0, 'X')

        elif (column != 6 and self.board[row[column] - 1] != 'X' or 'R') or (
                coordinate[0] == 0 and 'X' in self.board[row] is True):
            print(self.board[row])
            location = row
            for item in self.board[row:]:
                if item == 'X':
                    temp = self.board.pop(location)
                    self.board.insert(row, 'X')
                    break
                location += 1
            print(self.board[row])

        elif coordinate[0] != 6 and self.board[row[column] - 1] != 'X' or 'R':
            return False

        # tracker = 0
        # for square in column_squares:
        #     self.board[tracker][column] = square
        #     tracker += 1

        if temp == 'R':
            self.get_current_player().update_captured()
            if self.get_current_player() == self.p1:
                self.set_current_player(self.p2)
            else:
                self.set_current_player(self.p1)
        else:
            if self.get_current_player() == self.p1:
                self.set_current_player(self.p2)
            else:
                self.set_current_player(self.p1)

        return True

    def move_forward(self, coordinate):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        column = coordinate[1]
        row = 6-coordinate[0]
        column_squares = []
        temp = None
        for list in self.board:
            column_squares.append(list[column])

        column_squares.reverse()

        print(column_squares)
        print(coordinate)
        if row == 0 and 'X' not in column_squares:
            print('scenario1')
            temp = column_squares.pop()
            column_squares.insert(0, 'X')

        elif (row != 6 and column_squares[row - 1] == 'X') or (row == 0 and 'X' in column_squares):
            print('scenario2')
            location = row
            if 'X' in column_squares[row:]:
                for item in column_squares[row:]:
                    if item == 'X':
                        column_squares.pop(location)
                        column_squares.insert(row, 'X')
                        break
                    location += 1
            else:
                column_squares.insert(row, 'X')
                print(column_squares)
                temp = column_squares.pop()

        elif row != 6 and column_squares[row - 1] != 'X':
            print('scenario3')
            return False

        column_squares.reverse()

        tracker = 0
        for square in column_squares:
            self.board[tracker][column] = square
            tracker += 1

        if temp == 'R':
            self.get_current_player().update_captured()
            self.change_current_player()
        else:
            self.change_current_player()

        return True


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
        self.captured = 0

    def get_player_name(self):
        """
        Method to get the current turns player
        :return: player name
        """
        return self.name

    def get_player_color(self):
        """
        Method to get the games winner
        :return: player name
        """
        return self.color

    def update_captured(self):
        self.captured = 1



game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
game.create_board()
print('current player is', end=': ')
print(game.current_player)
game.make_move('PlayerA', (0,0), 'B')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())
game.make_move('PlayerB', (6,1), 'F')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())
game.make_move('PlayerA', (1,0), 'B')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())
game.make_move('PlayerB', (5,1), 'F')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())
game.make_move('PlayerA', (2,0), 'B')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())
game.make_move('PlayerB', (4,1), 'F')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())
print(game.p2.captured)
game.make_move('PlayerA', (0,1), 'B')
game.display_board()
print('current player is', end=': ')
print(game.current_player.get_player_name())




