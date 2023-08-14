import random


class Slot:
    def __init__(self):
        self.__table = [["--", "--", "--"],
                        ["--", "--", "--"],
                        ["--", "--", "--"]]

        self.__lines = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

        self.__symbole = ["9", "10", "ja", "qu", "ki", "as", "bo"]
        self.__connectedsymbole=[]

    def gettable(self):
        return self.__table

    def getLines(self):
        return self.__lines

    def roll(self):

        for c in range(len(self.__table)):
            n = 6
            for l in range(len(self.__table[c])):
                self.__table[l][c] = self.__symbole[random.randint(0, n)]
                if self.__table[l][c] == 'bo':
                    n = 5