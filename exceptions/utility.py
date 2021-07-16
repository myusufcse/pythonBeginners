def printStar():
    print(20 * "*")


def printHash():
    print(20 * "#")


import math as m


def pyramid(r):
    for i in range(1, r):
        print(m.ceil(abs(r - i) // 2) * "  ", i * "* ")

