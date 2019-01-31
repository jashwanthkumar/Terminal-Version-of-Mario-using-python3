from Board import printb,array
from Matrix import *
from alien import *
from append import *
from functools import wraps
from background import Background
import os
import time
import termios
import signal
import errno
import sys
TERMIOS = termios
timeout_value = 0.1
Health = 3
bck = Background()
init()
def timeout(seconds, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise Exception(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator


@timeout(0.1)
def getkey():
        start = time.time()
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
            c = os.read(fd, 1)
        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

class Mario:
    x=0
    y=5
    def man(self):
        matrix[45-Mario.y][Mario.x+1] = ' '
        matrix[45-Mario.y][Mario.x+2] = ' '
        matrix[45-Mario.y][Mario.x+3] = '#'
        matrix[45-Mario.y][Mario.x+4] = '#'
        matrix[45-Mario.y][Mario.x+5] = ' '
        matrix[45-Mario.y][Mario.x+6] = '#'
        matrix[45-Mario.y][Mario.x+7] = '#'
        matrix[45-Mario.y][Mario.x+8] = ' '
        matrix[44-Mario.y][Mario.x+1] = ' '
        matrix[44-Mario.y][Mario.x+2] = ' '
        matrix[44-Mario.y][Mario.x+3] = '#'
        matrix[44-Mario.y][Mario.x+4] = ' '
        matrix[44-Mario.y][Mario.x+5] = ' '
        matrix[44-Mario.y][Mario.x+6] = '#'
        matrix[44-Mario.y][Mario.x+7] = ' '
        matrix[44-Mario.y][Mario.x+8] = ' '
        matrix[43-Mario.y][Mario.x+1] = ' '
        matrix[43-Mario.y][Mario.x+2] = 'x'
        matrix[43-Mario.y][Mario.x+3] = 'x'
        matrix[43-Mario.y][Mario.x+4] = 'x'
        matrix[43-Mario.y][Mario.x+5] = 'x'
        matrix[43-Mario.y][Mario.x+6] = 'x'
        matrix[43-Mario.y][Mario.x+7] = 'x'
        matrix[43-Mario.y][Mario.x+8] = ' '
        matrix[42-Mario.y][Mario.x+1] = ' '
        matrix[42-Mario.y][Mario.x+2] = ' '
        matrix[42-Mario.y][Mario.x+3] = 'x'
        matrix[42-Mario.y][Mario.x+4] = 'x'
        matrix[42-Mario.y][Mario.x+5] = 'x'
        matrix[42-Mario.y][Mario.x+6] = 'x'
        matrix[42-Mario.y][Mario.x+7] = ' '
        matrix[42-Mario.y][Mario.x+8] = ' '
        matrix[41-Mario.y][Mario.x+1] = ' '
        matrix[41-Mario.y][Mario.x+2] = ' '
        matrix[41-Mario.y][Mario.x+3] = ' '
        matrix[41-Mario.y][Mario.x+4] = 'x'
        matrix[41-Mario.y][Mario.x+5] = 'x'
        matrix[41-Mario.y][Mario.x+6] = ' '
        matrix[41-Mario.y][Mario.x+7] = ' '
        matrix[41-Mario.y][Mario.x+8] = ' '
    def checkbottom(self):
        x=0
        for i in range(1,9):
            if matrix[46-Mario.y][Mario.x+i] != ' ':
                if matrix[46-Mario.y][Mario.x+i] != '^':
                    x=1
                    break
        if x==1:
            return 1
        else:
            return 0
    def checktop(self):
        y=0
        for i in range(1,9):
            if matrix[40-Mario.y][Mario.x+i] != ' ':
                if matrix[40-Mario.y][Mario.x+i] != '^':
                    y=1
                    break

        if y==1:
            return 1
        else:
            return 0
    def checkright(self):
        for i in range(1,6):
            if matrix[40-Mario.y+i][Mario.x+9] != ' ' :
                if matrix[40-Mario.y+i][Mario.x+9] != '^':
                    return 1
        return 0
    def checkleft(self):
        for i in range(1,6):
            if matrix[40-Mario.y+i][Mario.x] != ' ':
                if matrix[40-Mario.y+i][Mario.x+9] != '^':
                    return 1
        return 0
MAR = Mario()
count = 0
while True:
    if bck.valu() == -685:
        os.system('clear')
        print('LEVEL 1 COMPLETED')
        time.sleep(0.5)
        print('LEVEL 2')
        time.sleep(0.5)
        levelchange()
    if bck.valu() == -1084:
        os.system('clear')
        print('LEVEL 2 COMPLETED')
        time.sleep(0.5)
        print('CONGRATULATIONS!!! YOU WIN :-))')
        time.sleep(0.5)
        sys.exit()
    if reset == 1:
        Reset()
        Mario.x = 0
        Mario.y = 5
    if MAR.y < 5:
        livechange()
        Reset()
        Mario.x = 0
        Mario.y = 5
    for ali in alis:
        if ali.check() == 0:
            ali.delete(ali.past1)
            ali.past = ali.man()
            ali.past1 = ali.past
            ali.move()
        if ali.x + ali.var < 3:
            ali.f = 1
            ali.delete(ali.past1)
        if ali.checkleft() == 1 and ali.temp == -1:
            ali.change()
        if ali.checkright() == 1 and ali.temp == 1:
            ali.change()
        if ali.checktop() == 1:
            ali.f = 1
            if ali.c == 0:
                ScoreAlien()
                ali.c = 1
            ali.delete(ali.past1)
        if ali.checkbottom() == 0:
            ali.f=1
            ali.delete(ali.past1)
        if ali.f == 0 and ali.x + ali.var + back.valu() < 160 and matrix[38][ali.x + ali.var + back.valu()] == 'x':
            count += 1
            if count % 3 == 0:
                healthchange()
        if ali.f == 0 and ali.x + ali.var + back.valu() < 160 - 7 and matrix[38][ali.x + ali.var + back.valu() + 7] == 'x':
            count += 1
            if count % 3 == 0:
                healthchange()

    MAR.man()
    printb()
    while MAR.checkbottom() == 0:
        if bck.valu() == -685:
            os.system('clear')
            print('LEVEL 1 COMPLETED')
            time.sleep(0.5)
            print('LEVEL 2')
            time.sleep(0.5)
            levelchange()
        if bck.valu() == -1084:
            os.system('clear')
            print('LEVEL 2 COMPLETED')
            time.sleep(0.5)
            print('CONGRATULATIONS!!! YOU WIN :-))')
            time.sleep(0.5)
            sys.exit()
        try:
            k = getkey()
        except:
            k = None
        if k == b'q':
            sys.exit()
        if k == b'd':
            if Mario.x  < 71  and MAR.checkright() == 0:
                Mario.x = Mario.x + 1
            if Mario.x >= 71 and MAR.checkright() == 0:
                bck.displace()
        if k == b'a':
            if Mario.x > 0 and MAR.checkleft() == 0:
                Mario.x = Mario.x - 1
        Mario.y = Mario.y - 1
        for var in range(1,9):
            matrix[40-Mario.y][Mario.x+var] = ' '
        MAR.man()
        for ali in alis:
            if ali.check() == 0:
                ali.delete(ali.past1)
                ali.past = ali.man()
                ali.past1 = ali.past
                ali.move()
            if ali.x + ali.var < 3:
                ali.f = 1
                ali.delete(ali.past1)
            if ali.checkleft() == 1 and ali.temp == -1:
                ali.change()
            if ali.checkright() == 1 and ali.temp == 1:
                ali.change()
            if ali.checktop() == 1:
                ali.f = 1
                if ali.c == 0:
                    ali.c = 1
                    ScoreAlien()
                ali.delete(ali.past1)
            if ali.checkbottom() == 0:
                ali.f=1
                ali.delete(ali.past1)
        printb()

    '''while MAR.checkbottom() == 0:
        Mario.y = Mario.y - 1
        for i in range(1,9):
            matrix[40-Mario.y][Mario.x+i] = ' '
        MAR.man()
        printb()'''
    try:
        k = getkey()
    except:
        k = None
    if k == b'q':
        sys.exit()
    if k == b'd':
        if Mario.x  < 71 and MAR.checkright() == 0:
            Mario.x = Mario.x + 1
        if Mario.x >= 71 and MAR.checkright() == 0:
            bck.displace()
    if k == b'a':
        if Mario.x > 0  and MAR.checkleft() == 0:
            Mario.x = Mario.x - 1
    if k == b'w':
        jump=0
        while jump < 15 and MAR.checktop() == 0:
            if bck.valu() == -685:
                os.system('clear')
                print('LEVEL 1 COMPLETED')
                time.sleep(0.5)
                print('LEVEL 2')
                time.sleep(0.5)
                levelchange()
            if bck.valu() == -1084:
                os.system('clear')
                print('LEVEL 2 COMPLETED')
                time.sleep(0.5)
                print('CONGRATULATIONS!!! YOU WIN :-))')
                time.sleep(0.5)
                sys.exit()
            jump += 1
            try:
                k = getkey()
            except:
                k = None
            if k == b'q':
                sys.exit()
            if k == b'd':
                if Mario.x  < 71 and MAR.checkright() == 0:
                    Mario.x = Mario.x + 1
                if Mario.x >= 71 and MAR.checkright() == 0:
                    bck.displace()
            if k == b'a':
                if Mario.x > 0 and MAR.checkleft() == 0:
                    Mario.x = Mario.x - 1
            Mario.y = Mario.y + 1
            for var in range(1,9):
                matrix[46-Mario.y][Mario.x+var] = ' '
            for ali in alis:
                if ali.check() == 0:
                    ali.delete(ali.past1)
                    ali.past = ali.man()
                    ali.past1 = ali.past
                    ali.move()
                if ali.x + ali.var < 3:
                    ali.f = 1
                    ali.delete(ali.past1)
                if ali.checkleft() == 1 and ali.temp == -1:
                    ali.change()
                if ali.checkright() == 1 and ali.temp == 1:
                    ali.change()
                if ali.checktop() == 1:
                    if ali.c == 0:
                        ali.c = 1
                        ScoreAlien()
                    ali.f = 1
                    ali.delete(ali.past1)
                if ali.checkbottom() == 0:
                    ali.f=1
                    ali.delete(ali.past1)
            MAR.man()
            printb()
        if MAR.checktop() == 1:
            if bck.valu() - Mario.x <= -35 - 71 and bck.valu() - Mario.x  >= -42 - 71:
                array[0] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -65 - 71 and bck.valu() - Mario.x  >= -72 - 71:
                array[1] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -85 - 71 and bck.valu() - Mario.x  >= -92- 71:
                array[2] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -105 - 71 and bck.valu() - Mario.x  >= -112 - 71:
                array[3] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -248 - 71 and bck.valu() - Mario.x  >= -255 - 71:
                array[4] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -348 - 71 and bck.valu() - Mario.x  >= -355 - 71:
                array[5] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -465 - 71 and bck.valu() - Mario.x  >= -472 - 71:
                array[6] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -472 - 71 and bck.valu() - Mario.x  >= -479 - 71:
                array[7] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -479 - 71 and bck.valu() - Mario.x  >= -486 - 71:
                array[8] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -486 - 71 and bck.valu() - Mario.x  >= -493 - 71:
                array[9] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -493 - 71 and bck.valu() - Mario.x  >= -500 - 71:
                array[10] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -500 - 71 and bck.valu() - Mario.x  >= -507 - 71:
                array[11] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -507 - 71 and bck.valu() - Mario.x  >= -514 - 71:
                array[12] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -514 - 71 and bck.valu() - Mario.x  >= -521 - 71:
                array[13] = 1
                Scorebrick()
            if bck.valu() - Mario.x  <= -521 - 71 and bck.valu() - Mario.x  >= -528 - 71:
                array[14] = 1
                Scorebrick()
