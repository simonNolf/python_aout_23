import sys

import pygame as p

from logic import Logic
from player import Player
from Slot import Slot

Player = Player()
Slot = Slot()
Logic = Logic()



class GUI:
    def __init__(self):
        self.__dimimg = 250
        self.WIDTH = 900
        self.HEIGHT = 900
        self.__screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
        p.display.set_caption('ma machine à sous')
        self.background = self.__screen.fill((103, 199, 103))
        self.lineWidth = 10
        self.lineColor = (0, 0, 0)

    def chargimg(self):
        images = ["9", "10", "as", "bo", "ja", "ki", "qu"]
        loadimg = {}
        try:
            for image in images:
                loadimg[image] = p.transform.scale(p.image.load("images/" + image + ".png"),
                                                   (self.__dimimg, self.__dimimg))
            return loadimg
        except FileNotFoundError:
            print('fichier non trouvé')
            return loadimg


    def betButton(self):
        p.draw.rect(self.__screen, (0, 0, 0), (750, 0, 150, 120))
        font = p.font.Font('StalshineRegular.ttf', 18)
        bouton = font.render('changer votre mise', True, (103, 199, 103))
        self.__screen.blit(bouton, (760, 30))

    def changeBet(self):
        bet = Player.getBet()
        if bet < 500:
            bet *= 10
        else:
            bet = 10
        Player.setBet(bet)

    def displayBet(self):
        font = p.font.Font('StalshineRegular.ttf', 18)
        mise = font.render('MISE : ' + str(Player.getBet()) + '            ', True, (0,0,0), (103, 199, 103))
        self.__screen.blit(mise, (760, 150))

    def desspieces(self, screen, slot, img):
        try:
            for i in range(3):
                for x in range(3):
                    case = slot[i][x]
                    screen.blit(img[case],
                                p.Rect(i * self.__dimimg, x * self.__dimimg, self.__dimimg, self.__dimimg))
        except KeyError:
            print('image pas trouvées')

    def pygameLaunch(self):
        p.init()

    def mainloop(self):
        self.pygameLaunch()
        Slot.roll()
        ligne = []
        self.betButton()
        self.displayBet()
        while True:
            if Player.getpointsplayer() == 0:
                raise EnvironmentError("vous n'avez plus de points")
            for event in p.event.get():
                if Player.getBet() > Player.getpointsplayer():
                    a = Player.getBet()
                    if a > 10 :
                        a //= 10
                    else:
                        raise InterruptedError("vous n'avez plus assez de points")
                    Player.setBet(a)
                if event.type == p.QUIT:
                    sys.exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    pos = p.mouse.get_pos()
                    if pos[0]>750 and pos[1] <120:
                        self.changeBet()
                    else:
                        self.__screen.fill((103, 199, 103))
                        Slot.roll()
                        Logic.setcurrenttable(Slot.gettable())
                        Player.bet()
                        self.winPoints()
                        self.displayPoints()
                        ligne = self.getLine()
            self.desspieces(self.__screen, Slot.gettable(), self.chargimg())
            self.betButton()
            self.displayBet()
            self.drawLine(ligne)
            p.display.update()

    def startGame(self):
        self.mainloop()

    def displayPoints(self):
        font = p.font.Font('StalshineRegular.ttf', 20)
        score = font.render("vous avez "+ str(Player.getpointsplayer())+ " points", True, (0,0,0),(103, 199, 103))
        self.__screen.blit(score,(10, 850))

    def winPoints(self):
        a = Logic.Point(Player)
        multi = Player.getBet() // 10
        win = a
        if multi != 0:
            win = a *multi
        font = p.font.Font('StalshineRegular.ttf', 20)
        score = font.render("vous avez  gagné " + str(win) + " points", True, (0, 0, 0), (103, 199, 103))
        self.__screen.blit(score, (10, 800))

    def getLine(self):
        symbole = ""
        points = []
        count = 0
        for i in Logic.getLines():
            j = 0
            count += 1
            for x in i:
                j += 1
                if symbole == "":
                    symbole = Logic.currentTable[x[0]][x[1]]
                if symbole != Logic.currentTable[x[0]][x[1]]:
                    symbole = ""
                    j = 0
                    break
                if j % 3 == 0 and symbole != "":
                    points.append(count)
        return points

    def drawLine(self, x):
        if len(x) == 0 :
            pass
        else:
            for i in x:
                if i == 1 :
                    p.draw.line(self.__screen, self.lineColor, (0, 125), (750, 125), self.lineWidth)
                    p.display.flip()
                if i == 2:
                    p.draw.line(self.__screen, self.lineColor, (0, 375), (750, 375), self.lineWidth)
                    p.display.flip()
                if i == 3:
                    p.draw.line(self.__screen, self.lineColor, (0, 625), (750, 625), self.lineWidth)
                    p.display.flip()
                if i == 4:
                    p.draw.line(self.__screen, self.lineColor, (0, 0), (750, 750), self.lineWidth)
                    p.display.flip()
                if i == 5:
                    p.draw.line(self.__screen, self.lineColor, (0, 750), (750, 0), self.lineWidth)
                    p.display.flip()
