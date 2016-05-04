from setup import equality


class Rook:
    def __init__(self, input_color):
        """
        Initializes a rook that is capable of being compared to another rook,
        and returning a list of possible moves.
        :type input_color color.Color
        """
        self.color = input_color.color

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.color == self.color

    def possible_moves(self, location, position):
        """

        :type location: algebraic.Location
        :param position: board.Board
        """
        moves = []
        move = location

        move = move.shift_up()
        while equality.location_not_none(location) and position.is_square_empty(location):
            moves.append(move)
            move = move.shift_up()

        move = move.shift_down()
        while position.is_square_empty(location):
            moves.append(move)
            move = move.shift_down()

        move = move.shift_right()
        while position.is_square_empty(location):
            moves.append(move)
            move = move.shift_right()

        move = move.shift_left()
        while position.is_square_empty(location):
            moves.append(move)
            move = move.shift_left()
