import time
import os
matrix=[[' ' for x in range(160)] for y in range(160)]
array=[0 for x in range(100)]
tpis = []
pis = []
Health = 3
Lives = 3
Level = 1
Score = 0
reset = 0
def Scorebrick():
    global Score
    Score += 100
def ScoreAlien():
    global Score
    Score += 500
def score():
    global Score
    return Score
def level():
    global Level
    return Level
def levelchange():
    global Level
    Level += 1

def healthchange():
    global Health
    os.system('clear')
    print('Health reduced')
    time.sleep(1)
    Health -= 1
    if Health <= 0:
        livechange()
def health():
    return Health
def livechange():
    global Lives
    global Health
    Lives -= 1
    os.system('clear')
    print("YOU HAVE ONLY " + str(Lives) + " LIVES LEFT")
    Health = 3
    time.sleep(2)
    Reset()
    if Lives<=0:
        reset = 1
def lives():
    return Lives
def Reset():
    return reset
bris=[]
alis = []
clouds = []
hols = []
