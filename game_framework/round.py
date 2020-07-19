import random


class Round(object):
    def __init__(self, players, first_bid):
        # Players that were created in the game object. Each player has a hand of dominoes
        self.players = players

        # Indicates the trumps for this round
        # 0 = Blanks
        # 1 = Aces
        # 2 = Deuces
        # 3 = Treys
        # 4 = Fours
        # 5 = Fives
        # 6 = Sixes
        # 7 = Doubles
        # 8 = Follow Me

        self.trumps = -1
        self.curr_bid = 0
        self.first_bid = first_bid % 4

    def bid(self):
        player_with_highest_bid = 0
        current_bidder = self.first_bid

        DEBUG_BIDDING_STR = ''

        # Each Player bids
        for i in range(4):
            current_bid = self.players[current_bidder].bid(self.curr_bid, i + 1)

            DEBUG_BIDDING_STR += ('PLAYER # ' + str(current_bidder) + ' BIDS ' + str(current_bid) + '\n')

            if current_bid > self.curr_bid:
                self.curr_bid = current_bid
                player_with_highest_bid = current_bidder

            current_bidder = (current_bidder + 1) % 4

        self.trumps = self.players[player_with_highest_bid].set_trump()

        DEBUG_TRUMP_STRING = 'TRUMPS ARE ' + str(self.trumps) + '\n'

        for i in range(4):
            self.players[i].examine_dominoes(self.trumps)

        return player_with_highest_bid, DEBUG_BIDDING_STR, DEBUG_TRUMP_STRING

    def play_hand(self):
        return random.randint(1, 2)
