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
        self.winner = None

    def create_board(self):
        """
        Method to  initialize the board for start of game
        :return: a list of list as the board
        """
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
        Will check the current_player object and return playername
        :return: Player name
        """
        if self.current_player is None:
            return self.current_player
        else:
            return self.current_player.get_player_name()

    def set_current_player(self, player):
        """
        Method to set the current turns player
        :param player: player object
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
        Method to initiate a move.
        :param playername: Player name making the move
        :param coordinate: Coordinates of marble to move
        :param direction: One of the 4 directions to move
        :return: Either updated board with move, or will state invalid move and show the board again.
        """

        # Checks if there is a winner
        if self.winner is not None:
            return False

        #sets winner if no more marbles of either players color
        if 0 in self.get_marble_count():
            if self.get_marble_count()[0] == 0:
                if self.p1.color == 'B':
                    self.set_game_winner(self.p2)
                else:
                    self.set_game_winner(self.p1)
            if self.get_marble_count()[1] == 0:
                if self.p1.color == 'W':
                    self.set_game_winner(self.p2)
                else:
                    self.set_game_winner(self.p1)
            return False

        #Conditional for first move
        if self.current_player is None:
            if playername == self.p1.get_player_name():
                self. set_current_player(self.p1)
            else:
                self.set_current_player(self.p2)

        #Conditionals any moves other than first
        if playername == self.current_player.get_player_name() and self.current_player.get_player_color() == self.get_marble(coordinate):
            if direction == 'L':
                return self.move_left(coordinate)
            elif direction == 'R':
                return self.move_right(coordinate)
            elif direction == 'F':
                return self.move_forward(coordinate)
            elif direction == 'B':
                return self.move_backward(coordinate)

        else:
            return False


    def get_winner(self):
        """
        method to determine if there is a winner or not when called.
        :return: Player name or None
        """
        if self.winner is None:
            return None
        else:
            return self.winner.get_player_name()

    def get_captured(self, playername):
        """
        Method  to determine how many red marbles a player has captured.
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
        Method to determine the number of marbles on the board.
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
        :param player: player object
        """
        self.winner = player

    def get_current_turn(self):
        return self.current_player

    def move_backward(self, coordinate):
        """
        Method for determining if a move in this direction is valid and making that move if so
        :return: Boolean value for validity of move
        """

        column = coordinate[1]
        row = coordinate[0]
        column_squares = []
        temp = None

        #creates a list from the column to work with
        for list in self.board:
            column_squares.append(list[column])

        #scenario for moving an edge square with no blanks in the column
        if row == 0 and 'X' not in column_squares:
            temp = column_squares.pop()
            column_squares.insert(0, 'X')

        #scenario for any other square in a column with blank spaces within
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

        #scenario if the square to move does not have a blank square behind  it
        elif row != 6 and column_squares[row-1] != 'X':
            return False

        #updates board column with working column values
        tracker = 0
        for square in column_squares:
            self.board[tracker][column] = square
            tracker += 1

        #updates captured based on mable that fell off. Declares winner if 7 R is reached. Changes player afterwards.
        if temp == 'R':
            self.get_current_turn().update_captured()
            if self.current_player.captured == 7:
                self.set_game_winner(self.current_player)
                return True
            self.change_current_player()
        else:
            self.change_current_player()

        return True


    def move_left(self, coordinate):
        """
        Method for determining if a move in this direction is valid and making that move if so
        :return: Boolean value for validity of move
        """
        column = 6-coordinate[1]
        row = coordinate[0]
        working_row = self.board[row]
        temp = None

        #reverses a row to work with
        working_row.reverse()

        # scenario for moving an edge square with no blanks in the row
        if column == 0 and 'X' not in working_row:
            temp = working_row.pop()
            working_row.insert(0, 'X')

        # scenario for any other square in a row with blank spaces within
        elif (column != 6 and working_row[column - 1] == 'X') or (column == 0 and 'X' in working_row):
            location = column
            if 'X' in working_row[column:]:
                for item in working_row[column:]:
                    if item == 'X':
                        working_row.pop(location)
                        working_row.insert(column, 'X')
                        break
                    location += 1
            else:
                working_row.insert(column, 'X')
                temp = working_row.pop()

        # scenario if the square to move does not have a blank square behind  it
        elif column != 6 and working_row[column - 1] != 'X':
            return False

        #reverses final row again for insertion back into game board
        working_row.reverse()
        self.board[row] = working_row

        # updates captured based on mable that fell off. Declares winner if 7 R is reached. Changes player afterwards.
        if temp == 'R':
            self.get_current_turn().update_captured()
            if self.current_player.captured == 7:
                self.set_game_winner(self.current_player)
                return True
            self.change_current_player()
        else:
            self.change_current_player()

        return True

    def move_right(self, coordinate):
        """
        Method for determining if a move in this direction is valid
        :return: Boolean value for validity of move
        """
        column = coordinate[1]
        row = coordinate[0]
        working_row = self.board[row]
        temp = None

        # scenario for moving an edge square with no blanks in the column
        if column == 0 and 'X' not in working_row:
            temp = working_row.pop()
            working_row.insert(0, 'X')

        # scenario for any other square in a column with blank spaces within
        elif (column != 6 and working_row[column - 1] == 'X') or (column == 0 and 'X' in working_row):
            location = column
            if 'X' in working_row[column:]:
                for item in working_row[column:]:
                    if item == 'X':
                        working_row.pop(location)
                        working_row.insert(column, 'X')
                        break
                    location += 1
            else:
                working_row.insert(column, 'X')
                temp = working_row.pop()

        # scenario if the square to move does not have a blank square behind  it
        elif column != 6 and working_row[column - 1] != 'X':
            return False

        #inserts working row into game board
        self.board[row] = working_row

        # updates board column with working column values
        if temp == 'R':
            self.get_current_turn().update_captured()
            if self.current_player.captured == 7:
                self.set_game_winner(self.current_player)
                return True
            self.change_current_player()
        else:
            self.change_current_player()

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

        # creates a list from the column to work with
        for list in self.board:
            column_squares.append(list[column])

        #reverses column to work with
        column_squares.reverse()

        # scenario for moving an edge square with no blanks in the column
        if row == 0 and 'X' not in column_squares:
            temp = column_squares.pop()
            column_squares.insert(0, 'X')

        # scenario for any other square in a column with blank spaces within
        elif (row != 6 and column_squares[row - 1] == 'X') or (row == 0 and 'X' in column_squares):
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

        # scenario if the square to move does not have a blank square behind  it
        elif row != 6 and column_squares[row - 1] != 'X':
            return False

        #reverses row back to original order
        column_squares.reverse()

        # updates board column with working column values
        tracker = 0
        for square in column_squares:
            self.board[tracker][column] = square
            tracker += 1

        # updates captured based on mable that fell off. Declares winner if 7 R is reached. Changes player afterwards.
        if temp == 'R':
            self.get_current_turn().update_captured()
            if self.current_player.captured == 7:
                self.set_game_winner(self.current_player)
                return True
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
        """
        updates the captured count for a player
        """
        self.captured = 1





