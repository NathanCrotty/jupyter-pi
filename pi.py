accuracy = int(input("enter numeric accuracy (higher numbers run slower)\n")) * 1000

print("importing packages")
from random import random
import matplotlib.pyplot as plt
from decimal import Decimal
from math import sqrt

def in_circle(inx, iny, outx, outy):
    a = 0

    while True:
        if sqrt((inx[a] ** 2) + (iny[a] ** 2)) <= 1:
            outx.append(inx[a])
            outy.append(iny[a])
        a += 1
        if a >= len(iny):
            print(a)
            break

print("defining vatiables")
repititions = 0
x = []
y = []
circleX = []
circleY = []

npoints = 0
pi = 0
stop = False
print("creating random list")
while True:
    x.append(random())
    y.append(random())
    repititions += 1
    if stop == True:
        break
    if repititions >= accuracy:
        stop = True


in_circle(x, y, circleX, circleY)

print("plotting points")
#plt.scatter(circleX, circleY, s = 1)
#plt.show()
print("done")
print("π ≈ ", Decimal(4 * (len(circleX)/len(x))))
