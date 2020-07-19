from deck import *
from round import *


class Game(object):
    def __init__(self):
        self.team_1_score = 0  # players[0] and players[2]
        self.team_2_score = 0  # players[1] and players[3]
        self.first_bid = 0  # This value will increment each round to determine what player will bid first

    # Executes the game loop
    def play_game(self):
        round_num = 1
        while True:
            if self.team_1_score >= 7:
                print('Team 1 Won!')
                return
            elif self.team_2_score >= 7:
                print('Team 2 Won!')
                return
            else:
                players = Deck().deal()
                next_round = Round(players, self.first_bid)

                # start the bidding
                player_with_highest_bid = next_round.bid()

                winner = next_round.play_hand()

                if winner == 1:
                    self.team_1_score += 1
                else:
                    self.team_2_score += 1

                # Next player bids first
                self.first_bid = (self.first_bid + 1) % 4
                round_num += 1

    def print_game_state(self, round_num, players):
        print('ROUND NUMBER', str(round_num))
        print('-------------------------------------')
        print('PLAYER #', str(self.first_bid), 'BIDS FIRST\n')

        print_players(players)
        print('')
        print('TEAM 1 SCORE:', str(self.team_1_score))
        print('TEAM 2 SCORE:', str(self.team_2_score))
        print('\n')

    def assign_winner(self, winner):
        if winner == 0:
            self.team_1_score += 1
        else:
            self.team_2_score += 1


def print_players(players):
    print('PLAYER 1')
    players[0].hand.print()

    print('\nPLAYER 2')
    players[1].hand.print()

    print('\nPLAYER 3')
    players[2].hand.print()

    print('\nPLAYER 4')
    players[3].hand.print()


def pretty_print_players(players):
    print('PLAYER 1')
    players[0].hand.pretty_print()

    print('\nPLAYER 2')
    players[1].hand.pretty_print()

    print('\nPLAYER 3')
    players[2].hand.pretty_print()

    print('\nPLAYER 4')
    players[3].hand.pretty_print()
