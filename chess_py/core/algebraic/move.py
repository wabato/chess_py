# -*- coding: utf-8 -*-

"""
Class that stores chess moves.
Destination, status and piece making move are required
to initialize Move.

:type: end_loc: Location
:type: piece: Piece
:type: status: int

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

import warnings

from .location import Location


class Move:
    def __init__(self, end_loc, piece, status,
                 start_rank=None,
                 start_file=None,
                 promoted_to_piece=None):
        """
        Constructor to create move using object Location

        :type: end_loc: Location
        :type: piece: Piece
        :type: status: int
        """
        self._end_loc = end_loc
        self._status = status
        self._piece = piece
        self.color = piece.color
        self.start_rank = start_rank
        self.start_file = start_file
        self.promoted_to_piece = promoted_to_piece

        if not self.on_board():
            warnings.warn("Location of move must be on the board")

    @property
    def end_loc(self):
        return self._end_loc

    @end_loc.setter
    def end_loc(self, end_loc):
        warnings.warn("Mutating end_loc attribute in Move should not be done")
        self._end_loc = end_loc

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        warnings.warn("Mutating status attribute in Move should not be done")
        self._status = status

    @property
    def piece(self):
        return self._piece

    def __key(self):
        return self.end_loc, self.piece, self.status, \
               self.start_rank, self.start_file, self.promoted_to_piece

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Finds if move is same move as this one.
        :type: other: Move
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Cannot compare type {} with Move".format(type(other)))

        for index, item in enumerate(self.__key()):
            if not self._check_equals_or_none(item, other.__key()[index]):
                return False

        return True

    @staticmethod
    def _check_equals_or_none(var1, var2):
        """
        If either is None then return True,
        otherwise compare them and return
        if they are equal.

        :type: var1: object
        :type: var2: object
        :rtype: bool
        """
        if var1 is None or var2 is None:
            return True

        return var1 == var2

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """
        Finds string representation in long algebraic noatation

        :rtype: str
        """
        move_str = str(Location(self.start_rank, self.start_file)) + str(self._end_loc)

        if self.promoted_to_piece is not None:
            move_str += str(self.promoted_to_piece)

        return move_str

    @property
    def start_loc(self):
        """
        Finds start Location of move if specified.
        Otherwise throws an AttributeError

        :rtype: Location
        """
        if self.start_rank is None or self.start_file is None:
            raise AttributeError("start_rank and start_file must be specified")

        return Location(self.start_rank, self.start_file)

    def on_board(self):
        """
        Determines whether end Location of this Move
        is on the board.

        :rtype: bool
        """
        return self.end_loc.on_board()

    def would_move_be_promotion(self):
        """
        Finds if move from current location would be a promotion
        """
        return (self._end_loc.rank == 0 and not self.color) or \
                (self._end_loc.rank == 7 and self.color)
