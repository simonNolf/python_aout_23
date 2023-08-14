from Slot import Slot
from points import Points

Points = Points()

class Logic(Slot):
    def __init__(self):
        super().__init__()
        self.currentTable = None

    def Point(self, player):
        symbole = ""
        points = 0
        count= 0
        for i in self.getLines():
            j=0
            count +=1

            for x in i:
                j+= 1
                if symbole == "":
                    symbole = self.currentTable[x[0]][x[1]]
                if symbole != self.currentTable[x[0]][x[1]]:
                    symbole = ""
                    j = 0
                    break
            if symbole != "":
                points += Points.getwinningpoint(symbole)
        player.addpoints(points)
        return points

    def getcurrentTable(self):
        return self.currentTable

    def setcurrenttable(self,table):
        self.currentTable = table

