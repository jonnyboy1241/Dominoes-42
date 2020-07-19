from constants import *
import random


class Player(object):
    def __init__(self, hand):
        self.hand = hand

    # The current player bids based on their hand
    def bid(self, current_highest_bid, position):
        # ARTIFICIAL INTELLIGENCE COMPONENT #1 NEEDS TO GO HERE

        if position == 4:
            if current_highest_bid == 0:
                return 30

        bid = random.randint(20, 42)

        if bid < 30:
            return 0
        elif bid <= current_highest_bid:
            return 0

        return bid

    # This player won the bidding, need to set the trump
    def set_trump(self):
        # ARTIFICIAL INTELLIGENCE COMPONENT #2 NEEDS TO GO HERE
        return random.randint(0, 8)

    def examine_dominoes(self, trumps):
        for i in range(7):
            if is_trump(self.hand.dominoes[i], trumps):
                self.hand.dominoes[i].is_trump = True


def is_trump(domino, trumps):
    # Follow Me -- No trumps
    if trumps == 8:
        return False

    # Trumps are suits
    if 0 <= trumps <= 6:
        return domino.pips[0] == trumps or domino.pips[1] == trumps

    # Trumps are doubles
    if trumps == 7:
        return domino.pips[0] == domino.pips[1]

    if DEBUG:
        print('SOMETHING WENT VERY HORRIBLY WRONG, AND I DON\'T KNOW WHAT!')
        print('VALUE OF TRUMP:', str(trumps))
        exit(-1)
