class Player:
    def __init__(self):
        self.__points = 5000
        self.__bet = 10

    def addpoints(self, winningPoints):
        self.__points += winningPoints

    def getpointsplayer(self):
        return self.__points

    def getBet(self):
        return self.__bet

    def setBet(self, new_bet):
        self.__bet = new_bet

    def bet(self):
        self.__points -= self.__bet