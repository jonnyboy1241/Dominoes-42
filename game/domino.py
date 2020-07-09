borderStr = '.------.------.'


class Domino(object):
    __slots__ = ['pips', 'score']

    def __init__(self, pips):
        self.pips = pips

        score = pips[0] + pips[1]

        if score % 5 == 0:
            self.score = score
        else:
            self.score = 0

    def print_domino(self):
        print('(' + str(self.pips[0]) + ', ' + str(self.pips[1]) + ')\tSCORE: ' + str(self.score))

    def pretty_print_domino(self):
        top = '|'
        mid = '|'
        bot = '|'

        if self.pips[0] == 0:
            top += '      |'
            mid += '      |'
            bot += '      |'
        elif self.pips[0] == 1:
            top += '      |'
            mid += '  ()  |'
            bot += '      |'
        elif self.pips[0] == 2:
            top += '()    |'
            mid += '      |'
            bot += '    ()|'
        elif self.pips[0] == 3:
            top += '()    |'
            mid += '  ()  |'
            bot += '    ()|'
        elif self.pips[0] == 4:
            top += '()  ()|'
            mid += '      |'
            bot += '()  ()|'
        elif self.pips[0] == 5:
            top += '()  ()|'
            mid += '  ()  |'
            bot += '()  ()|'
        elif self.pips[0] == 6:
            top += '()  ()|'
            mid += '()  ()|'
            bot += '()  ()|'

        if self.pips[1] == 0:
            top += '      |'
            mid += '      |'
            bot += '      |'
        elif self.pips[1] == 1:
            top += '      |'
            mid += '  ()  |'
            bot += '      |'
        elif self.pips[1] == 2:
            top += '()    |'
            mid += '      |'
            bot += '    ()|'
        elif self.pips[1] == 3:
            top += '()    |'
            mid += '  ()  |'
            bot += '    ()|'
        elif self.pips[1] == 4:
            top += '()  ()|'
            mid += '      |'
            bot += '()  ()|'
        elif self.pips[1] == 5:
            top += '()  ()|'
            mid += '  ()  |'
            bot += '()  ()|'
        elif self.pips[1] == 6:
            top += '()  ()|'
            mid += '()  ()|'
            bot += '()  ()|'

        print(borderStr)
        print(top)
        print(mid)
        print(bot)
        print(borderStr + '\n')
