class Domino(object):
    __slots__ = ['pips']

    def __init__(self, pips):
        self.pips = pips

    def print_values(self):
        print(str(self.pips[0]) + ',' + str(self.pips[1]))
