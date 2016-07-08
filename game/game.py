"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from core.board import Board
from core.color import Color
from game.game_state import *
import itertools


class Game:
    def __init__(self, player_white, player_black):
        """
        Creates new game given the players.
        :type player_white: human.Player or ai
        :type player_black: human.Player or ai
        """
        print("beginning of init")
        self.player_white = player_white
        self.player_black = player_black
        self.position = Board.init_default()
        print("init was called")

    def start(self):
        self.play()

    def play(self):
        colors = [self.white_move(), self.black_move()]
        colors = itertools.cycle(colors)

        while True:
            color = next(colors)
            if no_moves(self.position):
                if self.position.get_king(Color.init_black()).in_check():
                    return 1

                elif self.position.get_king(Color.init_white()).in_check():
                    return 0
                else:
                    return 0.5

            color()

    def white_move(self):
        if no_moves(self.position):
            exit()
        move = self.player_white.generate_move(self.position)
        # TODO implement position change as a result of the move

    def black_move(self):
        move = self.player_black.generate_move(self.position)
        # TODO implement position change as a result of the move
