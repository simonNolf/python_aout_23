class Points:
    def __init__(self):
        self.__points = {
            "9": 3,
            "10": 5,
            "ja": 8,
            "qu": 11,
            "ki": 15,
            "as": 20,
            "bo": 25,
        }
    def getwinningpoint(self,connectedsymbole):
        return self.__points[connectedsymbole]


