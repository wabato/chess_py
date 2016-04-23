from setup import board


class Game:
    def __init__(self, player_white, player_black):
        """
        Creates new game given the players.
        :type player_white: human.Player or ai
        :type player_black: human.Player or ai
        """
        self.player_white = player_white
        self.player_black = player_black
        self.position = board.Board.init_default()

    def start(self):
        self.white_move()

    def white_move(self):
        move = self.player_white.generate_move(self.position)
        #TODO implement position change as a result of the move

    def black_move(self):
        move = self.player_black.generate_move(self.position)
        # TODO implement position change as a result of the move

