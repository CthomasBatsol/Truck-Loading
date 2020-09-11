import random
import os
import csv
import pdb
from itertools import permutations
import numpy as np
import pandas as pd

skid = pd.read_csv('data.csv')

class Pallets:
    pallets = []
    iu = []

    def __init__(self):
        self.assignPalletsInfo()

    def assignPalletsInfo(self):

        with open("data.csv") as fi:
            # Ignore first line
            for line in fi:
                # "1,100"
                info = line.split(",")
                # info = ["1","100"]
                palletWeight = int(info[1].replace('"','').replace('\n',''))
                # palletWeight = 1
                palletIu = int(info[0].replace('"',''))
                # palletIu = 100
                self.pallets.append(palletWeight)
                self.iu.append(palletIu)

class Truck:
    lowerLeftSide = []
    lowerRightSide = []
    upperLeftSide = []
    upperRightSide = []
    leftFrontLoad = 0
    leftBackLoad = 0
    rightBackLoad = 0
    rightFrontLoad = 0
    LeftCenterLoad = 0
    RightCenterLoad = 0
    leftLoad = 0
    rightLoad = 0
    frontLoad = 0
    backLoad = 0
    Load = 0
    p = Pallets()

    def fillVectors(self):
        self.lowerRightSide = []
        self.lowerLeftSide = []
        self.upperRightSide = []
        self.upperLeftSide = []
        random.shuffle(self.p.pallets)
        # pallets size could be even or odd
        if len(self.p.pallets) <= 24:
            # Even pallets
            self.lowerLeftSide = self.p.pallets[:12]
            self.lowerRightSide = self.p.pallets[12:]
        else:
            self.p.pallets.sort(reverse=True)
            lowerLevel = self.p.pallets[:24]
            upperLevel = self.p.pallets[24:]
            random.shuffle(lowerLevel)
            random.shuffle(upperLevel)              
            # Aqui é garantido que lowerLevel necessariamente tem pelo menos 25 posiçoes. 0-24
            # Ja que o if anterior verifica <= 24
            self.lowerLeftSide = lowerLevel[:12]
            self.lowerRightSide = lowerLevel[12:]
            addToleft = True
            # Intercala a inserçao em upperLeft e upperRight
            # upperLevel está ordenado do maior pro menor, entao o nivel de cima do caminhao
            # vai estar relativamente balanceado fora do centro.
            for p in upperLevel:
                if addToleft:
                    self.upperLeftSide.append(p)
                    addToleft = False
                else:
                    self.upperRightSide.append(p)
                    addToleft = True

    def calculatePalletDistribution(self):
        x = len(self.p.pallets)

        if x == 1:
            self.leftFrontLoad = self.lowerLeftSide[0]/2
            self.rightFrontLoad = self.lowerLeftSide[0]/2
            self.rightBackLoad = 0
            self.leftBackLoad = 0
            self.LeftCenterLoad = 0
            self.RightCenterLoad = 0

        elif x == 2:
            self.leftFrontLoad = self.lowerLeftSide[0]/2
            self.rightFrontLoad = self.lowerLeftSide[0]/2
            self.rightBackLoad = self.lowerLeftSide[1]/2
            self.leftBackLoad = self.lowerLeftSide[1]/2
            self.LeftCenterLoad = 0
            self.RightCenterLoad = 0

        elif x == 3:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:2])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:2])/2
            self.rightBackLoad = self.lowerLeftSide[2]/2
            self.leftBackLoad = self.lowerLeftSide[2]/2
            self.LeftCenterLoad = 0
            self.RightCenterLoad = 0

        elif x == 4:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:2])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:2])/2
            self.rightBackLoad = sum(self.lowerLeftSide[2:4])/2
            self.leftBackLoad = sum(self.lowerLeftSide[2:4])/2
            self.LeftCenterLoad = 0
            self.RightCenterLoad = 0

        elif x == 5:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:3])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:3])/2
            self.rightBackLoad = sum(self.lowerLeftSide[3:5])/2
            self.leftBackLoad = sum(self.lowerLeftSide[3:5])/2
            self.LeftCenterLoad = self.lowerLeftSide[3]
            self.RightCenterLoad = self.lowerLeftSide[3]

        elif x == 6:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:3])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:3])/2
            self.rightBackLoad = sum(self.lowerLeftSide[3:6])/2
            self.leftBackLoad = sum(self.lowerLeftSide[3:6])/2
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:4])
            self.RightCenterLoad = sum(self.lowerLeftSide[2:4])

        elif x == 7:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:4])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:4])/2
            self.rightBackLoad = sum(self.lowerLeftSide[4:7])/2
            self.leftBackLoad = sum(self.lowerLeftSide[4:7])/2
            self.LeftCenterLoad = sum(self.lowerLeftSide[3:5])
            self.RightCenterLoad = sum(self.lowerLeftSide[3:5])

        elif x == 8:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:4])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:4])/2
            self.rightBackLoad = sum(self.lowerLeftSide[4:8])/2
            self.leftBackLoad = sum(self.lowerLeftSide[4:8])/2
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:5])
            self.RightCenterLoad = 0

        elif x == 9:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:5])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:5])/2
            self.rightBackLoad = sum(self.lowerLeftSide[5:9])/2
            self.leftBackLoad = sum(self.lowerLeftSide[3:6])
            self.LeftCenterLoad = sum(self.lowerLeftSide[3:6])
            self.RightCenterLoad = 0

        elif x == 10:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:5])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:5])/2
            self.rightBackLoad = sum(self.lowerLeftSide[5:10])/2
            self.leftBackLoad = sum(self.lowerLeftSide[5:10])/2
            self.LeftCenterLoad = 0
            self.RightCenterLoad = 0

        elif x == 11:
            self.rightFrontLoad = sum(self.lowerLeftSide[0:6])/2
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6])/2
            self.rightBackLoad = sum(self.lowerLeftSide[6:11])/2
            self.leftBackLoad = sum(self.lowerLeftSide[6:11])/2
            self.LeftCenterLoad = 0
            self.RightCenterLoad = 0

        elif x == 12:
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6])/2
            self.rightFrontLoad = sum(self.lowerLeftSide[0:6])/2
            self.rightBackLoad = sum(self.lowerRightSide[6:12])/2
            self.leftBackLoad = sum(self.lowerLeftSide[6:12])/2
            self.LeftCenterLoad = sum(self.lowerLeftSide[4:8])
            self.RightCenterLoad = sum(self.lowerLeftSide[4:8])

        elif x == 13:
            self.rightFrontLoad = self.lowerRightSide[0] + \
                sum(self.lowerLeftSide[0:5])/2
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + self.lowerRightSide[0]/2
            self.rightBackLoad = sum(self.lowerLeftSide[6:12])/2
            self.leftBackLoad = sum(self.lowerLeftSide[6:12])/2
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[3:5])/2 + self.lowerLeftSide[5] + sum(self.lowerLeftSide[6:8])/2
            self.RightCenterLoad = self.lowerRightSide[0] + sum(
                self.lowerLeftSide[3:5])/2 + sum(self.lowerLeftSide[6:8])/2

        elif x == 14:
            self.rightFrontLoad = sum(
                self.lowerLeftSide[0:5])/2 + self.lowerRightSide[0]
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:5])/2 + self.lowerLeftSide[5]
            self.rightBackLoad = self.lowerRightSide[1] + \
                sum(self.lowerLeftSide[7:12])/2
            self.leftBackLoad = sum(
                self.lowerLeftSide[7:12])/2 + self.lowerLeftSide[6]
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[5:7]) + sum(self.lowerLeftSide[3:5])/2 + self.lowerLeftSide[7]/2
            self.RightCenterLoad = sum(
                self.lowerRightSide[0:2]) + sum(self.lowerLeftSide[3:5])/2 + self.lowerLeftSide[7]/2

        elif x == 15:
            self.rightFrontLoad = sum(self.lowerRightSide[0:2]) + sum(self.lowerLeftSide[0:4])/2
            self.leftFrontLoad = sum(self.lowerLeftSide[4:6]) + sum(self.lowerLeftSide[0:4])/2
            self.rightBackLoad = self.lowerRightSide[2] + sum(self.lowerLeftSide[7:12])/2
            self.leftBackLoad = self.lowerLeftSide[6] + sum(self.lowerLeftSide[7:12])/2
            self.LeftCenterLoad = sum(self.lowerLeftSide[4:7])
            self.RightCenterLoad = sum(self.lowerRightSide[0:3])

        elif x == 16:
            self.rightFrontLoad = sum(
                self.lowerLeftSide[0:4])/2 + sum(self.lowerRightSide[0:2])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:4])/2 + sum(self.lowerLeftSide[4:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[2:4]) + sum(self.lowerLeftSide[8:12])/2
            self.leftBackLoad = sum(
                self.lowerLeftSide[8:12])/2 + sum(self.lowerLeftSide[6:8])
            self.LeftCenterLoad = sum(self.lowerLeftSide[4:8])
            self.RightCenterLoad = sum(self.lowerRightSide[0:4])

        elif x == 17:
            self.rightFrontLoad = sum(
                self.lowerLeftSide[0:4])/2 + sum(self.lowerRightSide[0:2])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:4])/2 + sum(self.lowerLeftSide[4:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[2:5]) + sum(self.lowerLeftSide[9:12])/2
            self.leftBackLoad = sum(
                self.lowerLeftSide[9:12])/2 + sum(self.lowerLeftSide[6:9])
            self.LeftCenterLoad = sum(self.lowerLeftSide[4:7])
            self.RightCenterLoad = sum(self.lowerRightSide[0:3])

        elif x == 18:
            self.rightFrontLoad = sum(self.lowerLeftSide[0:3])/2 + sum(self.lowerRightSide[0:3])
            self.leftFrontLoad = sum(self.lowerLeftSide[0:3])/2 + sum(self.lowerLeftSide[3:6])
            self.rightBackLoad = sum(self.lowerRightSide[3:6]) + sum(self.lowerLeftSide[9:12])/2
            self.leftBackLoad = sum(self.lowerLeftSide[9:12])/2 + sum(self.lowerLeftSide[6:9])
            self.LeftCenterLoad = sum(self.lowerLeftSide[4:7])
            self.RightCenterLoad = sum(self.lowerRightSide[1:4])

        elif x == 19:
            self.rightFrontLoad = sum(
                self.lowerLeftSide[0:3])/2 + sum(self.lowerRightSide[0:3])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:3])/2 + sum(self.lowerLeftSide[3:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[3:7]) + sum(self.lowerLeftSide[10:12])/2
            self.leftBackLoad = sum(
                self.lowerLeftSide[10:12])/2 + sum(self.lowerLeftSide[6:10])
            self.LeftCenterLoad = sum(self.lowerLeftSide[3:9])
            self.RightCenterLoad = sum(self.lowerRightSide[0:6])

        elif x == 20:
            self.rightFrontLoad = sum(
                self.lowerLeftSide[0:2])/2 + sum(self.lowerRightSide[0:4])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:2])/2 + sum(self.lowerLeftSide[2:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[4:8]) + sum(self.lowerLeftSide[10:12])/2
            self.leftBackLoad = sum(
                self.lowerLeftSide[10:12])/2 + sum(self.lowerLeftSide[6:10])
            self.LeftCenterLoad = sum(self.lowerLeftSide[3:9])
            self.RightCenterLoad = sum(self.lowerRightSide[1:7])

        elif x == 21:
            self.rightFrontLoad = sum(
                self.lowerLeftSide[0:2])/2 + sum(self.lowerRightSide[0:4])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:2])/2 + sum(self.lowerLeftSide[2:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[4:9]) + self.lowerLeftSide[11]/2
            self.leftBackLoad = self.lowerLeftSide[11] / \
                2 + sum(self.lowerLeftSide[6:11])
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:9])
            self.RightCenterLoad = sum(self.lowerRightSide[0:7])

        elif x == 22:
            self.rightFrontLoad = self.lowerLeftSide[0] / \
                2 + sum(self.lowerRightSide[0:5])
            self.leftFrontLoad = self.lowerLeftSide[0] / \
                2 + sum(self.lowerLeftSide[1:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[5:10]) + self.lowerLeftSide[11]/2
            self.leftBackLoad = self.lowerLeftSide[11] / \
                2 + sum(self.lowerLeftSide[6:11])
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:10])
            self.RightCenterLoad = sum(self.lowerRightSide[0:8])

        elif x == 23:
            self.rightFrontLoad = self.lowerLeftSide[0]/2 + sum(self.lowerRightSide[0:5])
            self.leftFrontLoad = self.lowerLeftSide[0]/2 + sum(self.lowerLeftSide[1:6]) 
            self.rightBackLoad = sum(self.lowerRightSide[5:11])
            self.leftBackLoad = sum(self.lowerRightSide[6:12])
            self.LeftCenterLoad = sum(self.lowerLeftSide[3:9])
            self.RightCenterLoad = sum(self.lowerRightSide[2:8])

        elif x == 24:
            self.rightFrontLoad = sum(self.lowerRightSide[0:6])
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6])
            self.rightBackLoad = sum(self.lowerRightSide[6:12])
            self.leftBackLoad = sum(self.lowerLeftSide[6:12])
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:10])
            self.RightCenterLoad = sum(self.lowerRightSide[2:10])

        if x == 25:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + self.upperLeftSide[0]
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6])
            self.rightBackLoad = sum(self.lowerRightSide[6:12])
            self.leftBackLoad = sum(self.lowerLeftSide[6:12])
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:10])
            self.RightCenterLoad = sum(self.lowerRightSide[2:10])

        elif x == 26:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + self.upperLeftSide[0]
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + self.upperRightSide[0]
            self.rightBackLoad = sum(self.lowerRightSide[6:12])
            self.leftBackLoad = sum(self.lowerLeftSide[6:12])
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:10])
            self.RightCenterLoad = sum(self.lowerRightSide[2:10])

        elif x == 27:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + self.upperLeftSide[0]
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + self.upperRightSide[0]
            self.rightBackLoad = sum(self.lowerRightSide[6:12])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + self.upperLeftSide[1]
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:10])
            self.RightCenterLoad = sum(self.lowerRightSide[2:10])

        elif x == 28:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + self.upperLeftSide[0]
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + self.upperRightSide[0]
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + self.upperRightSide[1]
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + self.upperLeftSide[1]
            self.LeftCenterLoad = sum(self.lowerLeftSide[2:10])
            self.RightCenterLoad = sum(self.lowerRightSide[2:10])

        elif x == 29:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:2])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:2])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + self.upperLeftSide[2]
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + self.upperLeftSide[2]
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:3])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:2])

        elif x == 30:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:2])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:2])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + self.upperRightSide[2]
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + self.upperLeftSide[2]
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:3])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:3])

        elif x == 31:
            self.rightFrontLoad = sum(self.lowerRightSide[0:6]) + self.upperRightSide[0]
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6]) + self.upperLeftSide[0]
            self.rightBackLoad = sum(self.lowerRightSide[6:12]) + sum(self.upperRightSide[1:3])
            self.leftBackLoad = sum(self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[2:4])
            self.LeftCenterLoad = sum(self.lowerLeftSide[3:10]) + sum(self.upperLeftSide[0:4])
            self.RightCenterLoad = sum(self.lowerRightSide[3:10]) + sum(self.upperRightSide[0:3])

        elif x == 32:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:2])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:2])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[2:4])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[2:4])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:4])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:4])

        elif x == 33:
            self.rightFrontLoad = sum(self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:2])
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:2])
            self.rightBackLoad = sum(self.lowerRightSide[6:12]) + sum(self.upperRightSide[2:4])
            self.leftBackLoad = sum(self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[2:5])
            self.LeftCenterLoad = sum(self.lowerLeftSide[4:8]) + sum(self.upperLeftSide[0:5])
            self.RightCenterLoad = sum(self.lowerRightSide[4:8]) + sum(self.upperRightSide[0:4])

        elif x == 34:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:3])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:3])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[3:5])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[3:5])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:5])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:5])

        elif x == 35:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:3])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:4])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[3:5])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[4:6])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:6])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:5])

        elif x == 36:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:3])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:3])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[3:6])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[3:6])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:6])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:6])

        elif x == 37:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:3])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:4])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[3:6])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[4:7])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[1:7])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:6])

        elif x == 38:
            self.rightFrontLoad = sum(self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:4])
            self.leftFrontLoad = sum(self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:4])
            self.rightBackLoad = sum(self.lowerRightSide[6:12]) + sum(self.upperRightSide[4:7])
            self.leftBackLoad = sum(self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[4:7])
            self.LeftCenterLoad = sum(self.lowerLeftSide[5:9]) + sum(self.upperLeftSide[2:6])
            self.RightCenterLoad = sum(self.lowerRightSide[5:9]) + sum(self.upperRightSide[2:6])

        elif x == 39:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:4])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:4])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[4:7])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[4:8])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[1:7])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[1:7])

        elif x == 40:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:4])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:4])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[4:8])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[4:8])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[1:7])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[1:7])

        elif x == 41:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:4])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:5])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[4:8])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[5:9])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[2:8])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[1:7])

        elif x == 42:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:5])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:5])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[5:9])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[5:9])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[2:8])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[2:8])

        elif x == 43:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:5])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:5])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[5:9])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[5:10])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[2:8])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[2:8])

        elif x == 44:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:5])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:5])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[5:10])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[5:10])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[2:8])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[2:8])

        elif x == 45:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:5])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[5:10])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[6:11])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[3:9])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[2:7])

        elif x == 46:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:6])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[6:11])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[6:11])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[3:9])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[3:9])

        elif x == 47:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:6])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[6:11])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[6:12])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[0:6])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[0:6])

        elif x == 48:
            self.rightFrontLoad = sum(
                self.lowerRightSide[0:6]) + sum(self.upperRightSide[0:6])
            self.leftFrontLoad = sum(
                self.lowerLeftSide[0:6]) + sum(self.upperLeftSide[0:6])
            self.rightBackLoad = sum(
                self.lowerRightSide[6:12]) + sum(self.upperRightSide[6:12])
            self.leftBackLoad = sum(
                self.lowerLeftSide[6:12]) + sum(self.upperLeftSide[6:12])
            self.LeftCenterLoad = sum(
                self.lowerLeftSide[2:10]) + sum(self.upperLeftSide[2:10])
            self.RightCenterLoad = sum(
                self.lowerRightSide[2:10]) + sum(self.upperRightSide[2:10])
        else:
            breakpoint

        self.leftLoad = self.leftFrontLoad + self.leftBackLoad
        self.rightLoad = self.rightFrontLoad + self.rightBackLoad
        self.frontLoad = self.leftFrontLoad + self.rightFrontLoad
        self.backLoad = self.leftBackLoad + self.rightBackLoad

        loads = [
            (self.frontLoad/sum(self.p.pallets)-0.5)**2,
            (self.backLoad/sum(self.p.pallets)-0.5)**2,
            (self.rightFrontLoad/sum(self.p.pallets)-0.25)**2,
            (self.rightBackLoad/sum(self.p.pallets)-0.25)**2,
            (self.leftFrontLoad/sum(self.p.pallets)-0.25)**2,
            (self.leftBackLoad/sum(self.p.pallets)-0.25)**2,
            (self.LeftCenterLoad/sum(self.p.pallets)-0.35)**2,
            (self.RightCenterLoad/sum(self.p.pallets)-0.35)**2,
            (self.leftLoad/sum(self.p.pallets)-0.5)**2,
            (self.rightLoad/sum(self.p.pallets)-0.5)**2
        ]
    # Average}
        return sum(loads)/len(loads)

    def palletDistributionSimulation(self):
        final_average = 1000
        for i in range(0, 100000):
            self.fillVectors()
            average = self.calculatePalletDistribution()
            if average < final_average:
                final_average = average
                self.writeToFile(average)

    def writeToFile(self, average):

        f = open("load_layout.csv", "w")
        f.write(f"Truck load layout:\n")
        f.write(f"\n1st layer of pallets,,1,2,3,4,5,6,7,8,9,10,11,12")

        if len(self.p.pallets) >= 0 and len(self.p.pallets) < 12:

            f.write(f"\nTruck Cabin,""Left "",")

            if len(self.p.pallets) == 1 or len(self.p.pallets) == 2:
                f.write(f",,,,,{self.lowerLeftSide}")
            elif len(self.p.pallets) == 3 or len(self.p.pallets) == 4:
                f.write(f",,,,{self.lowerLeftSide}")
            elif len(self.p.pallets) == 5 or len(self.p.pallets) == 6:
                f.write(f",,,{self.lowerLeftSide}")
            elif len(self.p.pallets) == 7 or len(self.p.pallets) == 8:
                f.write(f",,{self.lowerLeftSide}")
            elif len(self.p.pallets) == 9 or len(self.p.pallets) == 10:
                f.write(f",{self.lowerLeftSide}")
            else:
                f.write(f"{self.lowerLeftSide}")

        elif len(self.p.pallets) >= 12 and len(self.p.pallets) < 24:

            if len(self.p.pallets) == 13 or len(self.p.pallets) == 14:
                f.write(f"\nTruck Cabin,""Right"",")
                f.write(f",,,,,{self.lowerRightSide}")
            elif len(self.p.pallets) == 15 or len(self.p.pallets) == 16:
                f.write(f"\nTruck Cabin,""Right"",")
                f.write(f",,,,{self.lowerRightSide}")
            elif len(self.p.pallets) == 17 or len(self.p.pallets) == 18:
                f.write(f"\nTruck Cabin,""Right"",")
                f.write(f",,,{self.lowerRightSide}")
            elif len(self.p.pallets) == 19 or len(self.p.pallets) == 20:
                f.write(f"\nTruck Cabin,""Right"",")
                f.write(f",,{self.lowerRightSide}")
            elif len(self.p.pallets) == 21 or len(self.p.pallets) == 22 or len(self.p.pallets) == 23:
                f.write(f"\nTruck Cabin,""Right"",")
                f.write(f",{self.lowerRightSide}")
            else:
                f.write(f"\nTruck Cabin,""Right"",")
                f.write(f"{self.lowerRightSide}")

            f.write(f"\nTruck Cabin,""Left "",")
            f.write(f"{self.lowerLeftSide}")

        else:

            f.write(f"\nTruck Cabin,""Right"",")
            f.write(f"{self.lowerRightSide}")
            f.write(f"\nTruck Cabin,""Left "",")
            f.write(f"{self.lowerLeftSide}")
            f.write(f"\n\n2nd layer of pallets,,1,2,3,4,5,6,7,8,9,10,11,12")
            f.write(f"\nTruck Cabin,""Right "",")

            if len(self.p.pallets) == 25 or len(self.p.pallets) == 26 or len(self.p.pallets) == 27 or len(self.p.pallets) == 28:
                f.write(f",,,,,{self.upperRightSide}")
                f.write(f"\nTruck Cabin,""Left "",")
                f.write(f",,,,,{self.upperLeftSide}")
            elif len(self.p.pallets) == 29 or len(self.p.pallets) == 30 or len(self.p.pallets) == 31 or len(self.p.pallets) == 32:
                f.write(f",,,,{self.upperRightSide}")
                f.write(f"\nTruck Cabin,""Left "",")
                f.write(f",,,,{self.upperLeftSide}")
            elif len(self.p.pallets) == 33 or len(self.p.pallets) == 34 or len(self.p.pallets) == 35 or len(self.p.pallets) == 36:
                f.write(f",,,,{self.upperRightSide}")
                f.write(f"\nTruck Cabin,""Left "",")
                f.write(f",,,,{self.upperLeftSide}")
            elif len(self.p.pallets) == 37 or len(self.p.pallets) == 38 or len(self.p.pallets) == 39 or len(self.p.pallets) == 40:
                f.write(f",,{self.upperRightSide}")
                f.write(f"\nTruck Cabin,""Left "",")
                f.write(f",,{self.upperLeftSide}")
            elif len(self.p.pallets) == 41 or len(self.p.pallets) == 42 or len(self.p.pallets) == 43 or len(self.p.pallets) == 44:
                f.write(f",{self.upperRightSide}")
                f.write(f"\nTruck Cabin,""Left "",")
                f.write(f",{self.upperLeftSide}")
            else:
                f.write(f"{self.upperRightSide}")
                f.write(f"\nTruck Cabin,""Left "",")
                f.write(f"{self.upperLeftSide}")

        f.write(f"\n\nInstructions:\n")
        f.write(f"\n1. If the pallet is alone from side to side of the layout it is actually centered in the truck.")
        f.write(f"\n2. Every blank cell means there is not pallet in that location.\n")

        f.write(f"\nLeft:"",")
        f.write(f"{self.leftLoad}")        
        f.write(f"\nRight:"",")
        f.write(f"{self.rightLoad}")          
        f.write(f"\nFront:"",")
        f.write(f"{self.frontLoad}")
        f.write(f"\nBack:"",")
        f.write(f"{self.backLoad}")
        f.write(f"\nLeft Front:"",")
        f.write(f"{self.leftFrontLoad}")
        f.write(f"\nRight Front:"",")
        f.write(f"{self.rightFrontLoad}")
        f.write(f"\nLeft Back:"",")
        f.write(f"{self.leftBackLoad}")
        f.write(f"\nRight Back:"",")
        f.write(f"{self.rightBackLoad}\n")
        f.close()

t = Truck()
t.palletDistributionSimulation()
skid.head()
