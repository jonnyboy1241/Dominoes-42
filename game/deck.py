from domino import *
from player import *
import random  # For shuffling the deck


# Base class for inheriting collections of dominoes
# (Deck has 28, Hand starts with 7, Trick has 4)
class DominoCollection(object):
    def print(self):
        for domino in self.dominoes:
            domino.print_domino()

    def pretty_print(self):
        for domino in self.dominoes:
            domino.pretty_print_domino()


class Deck(DominoCollection):
    def __init__(self):
        dominoes = []
        for i in range(7):
            for j in range(i, 7):
                dominoes.append(Domino((i, j)))

        self.dominoes = dominoes
        self.shuffle()

    def shuffle(self):
        random.seed()
        random.shuffle(self.dominoes)

    # Deals 7 dominoes to each player
    def deal(self):
        return Player(Hand(self.dominoes[0:7]), 1), \
               Player(Hand(self.dominoes[7:14]), 2), \
               Player(Hand(self.dominoes[14:21]), 3), \
               Player(Hand(self.dominoes[21:28]), 4)


class Hand(DominoCollection):
    def __init__(self, domino_collection):
        assert(len(domino_collection) == 7)
        self.dominoes = domino_collection


class Trick(DominoCollection):
    def __init__(self):
        self.dominoes = []
