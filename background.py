from random import *
from Board import *
var = 0
class Background:
    def __init__(self):
        pass
    def displace(self):
        global var
        var = var - 1
    def valu(self):
        global var
        return var

back = Background()
def holes():
    return 259+var
def pipes():
    return 300+var
def bricks1():
    return 110+var
def bricks2():
    return 140+var
def bricks3():
    return 160+var
def bricks4():
    return 180+var
def bricks5():
    return 323+var
def bricks6():
    return 423+var
def bricks7():
    return 540+var
def bricks8():
    return 547+var
def bricks9():
    return 554+var
def bricks10():
    return 561+var
def bricks11():
    return 568+var
def bricks12():
    return 575+var
def bricks13():
    return 582+var
def bricks14():
    return 589+var
def tpipes():
    return 300+var
def aliens():
    return 350+var
def clouds1():
    return 350+var
def clouds2():
    return 370+var
def clouds3():
    return 390+var
def Reset():
    reset = 0
    var = 0
