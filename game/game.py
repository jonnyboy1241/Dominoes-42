from deck import *


class Game(object):
    def __init__(self):
        self.hand1, self.hand2, self.hand3, self.hand4 = Deck().deal()
