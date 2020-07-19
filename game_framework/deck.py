from domino import *
from player import *
from constants import * # Constants for Debugging purposes right now
import random  # For shuffling the deck


# Base class for inheriting collections of dominoes
# (Deck has 28, Hand starts with 7, Trick has 4)
class DominoCollection(object):
    def __init__(self):
        self.dominoes = []

    def print(self):
        for domino in self.dominoes:
            domino.print_domino()

    def pretty_print(self):
        for domino in self.dominoes:
            domino.pretty_print_domino()


class Deck(DominoCollection):
    def __init__(self):
        super().__init__()
        for i in range(7):
            for j in range(i, 7):
                self.dominoes.append(Domino((i, j)))

        if DEBUG:
            assert len(self.dominoes) == 28

        self.shuffle()

    def shuffle(self):
        random.seed()
        random.shuffle(self.dominoes)

    # Deals 7 dominoes to each player
    def deal(self):
        player1 = Player(Hand(self.dominoes[0:7]))
        player2 = Player(Hand(self.dominoes[7:14]))
        player3 = Player(Hand(self.dominoes[14:21]))
        player4 = Player(Hand(self.dominoes[21:28]))

        return [player1, player2, player3, player4]


class Hand(DominoCollection):
    def __init__(self, domino_collection):
        super().__init__()

        if DEBUG:
            assert(len(domino_collection) == 7)

        self.dominoes = domino_collection


class Trick(DominoCollection):
    def __init__(self):
        super().__init__()
