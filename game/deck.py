from domino import *
import random   # For shuffling the deck


class Deck(object):
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

    # Really only for testing purposes
    def print_deck(self):
        for domino in self.dominoes:
            domino.print_values()