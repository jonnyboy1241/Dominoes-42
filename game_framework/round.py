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
        self.first_bid = first_bid

    def bid(self):
        player_with_highest_bid = 0
        current_bidder = self.first_bid

        # Each Player bids
        for i in range(4):
            current_bid = self.players[current_bidder].bid(self.curr_bid, i + 1)

            if current_bid > self.curr_bid:
                self.curr_bid = current_bid
                player_with_highest_bid = current_bidder

            current_bidder = (current_bidder + 1) % 4

        self.trumps = self.players[player_with_highest_bid].set_trump()

        for i in range(4):
            self.players[i].mark_trumps_in_hand(self.trumps)

    def play_hand(self):
        return random.randint(1, 2)
