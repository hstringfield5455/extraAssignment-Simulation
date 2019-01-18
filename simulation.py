# simulation.py
# by Holden Stringfield
# simulate rolling of dice

import random as r
import graphics as g


def main():
    num = getVals()
    rate = simulateRolls()
    #drawResults(num, rate)


def getVals():
    num = int(input("How many times do you want the program to run? "))
    return num


def simulateRolls(num):
    win = g.GraphWin("Dice Win", 500, 50)
    rate = 0
    for i in range(num):
        diceList = simulRoll()
        drawDice(diceList, win)
        #rate += findRolls(diceList)
    #return rate


def simulRoll():
    diceList = []
    for i in range(5):
        diceList.append(r.randint(1, 6))
    return diceList


def drawDice(diceList, win):
    for i in range(5):
        dice(diceList[i], win, i * 100)


def dice(diceNum, win, xval):
    p1 = g.Point(10, xval)
    p2 = g.Point(110, xval)
    r1 = g.Rectangle(p1, p2)
    r1.draw(win)
    diceNums(diceNum, win, xval)


#def rect(win, xval):
    #p1 = g.Point(10, xval)
    #p2 = g.Point(110, xval)
    #r1 = g.Rectangle(p1, p2)
    #r1.draw(win)


def diceNums(diceNum, win, xval):
    if diceNum == 1:

    if diceNum == 2:

    if diceNum == 3:

    if diceNum == 4:

    if diceNum == 5:

    if diceNum == 6:



#def returnStats(num, rate):


