from deck import *
from player import *


class Game(object):
    def __init__(self):
        self.player1, self.player2, self.player3, self.player4 = Deck().deal()

    def print_players(self):
        print('PLAYER 1')
        self.player1.hand.print()

        print('\nPLAYER 2')
        self.player2.hand.print()

        print('\nPLAYER 3')
        self.player3.hand.print()

        print('\nPLAYER 4')
        self.player4.hand.print()

    def pretty_print_players(self):
        print('PLAYER 1')
        self.player1.hand.pretty_print()

        print('\nPLAYER 2')
        self.player2.hand.pretty_print()

        print('\nPLAYER 3')
        self.player3.hand.pretty_print()

        print('\nPLAYER 4')
        self.player4.hand.pretty_print()