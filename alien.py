import os
from colorama import *
from Matrix import *
from background import *
back = Background()
class Alien:
        past = 0
        past1 = 0
        x=0
        y=5
        f = 0
        count = 0
        c = 0
        def __init__(self,var,temp):
            self.temp = temp
            self.var = var
        def check(self):
            return self.f
        def change(self):
            self.temp = -self.temp
        def move(self):
            self.count += 1
            if level() == 1:
                if self.count % 3 == 0:
                    self.var += self.temp
            else:
                self.var += self.temp
        def man(self):
            try:
                matrix[45-Alien.y][Alien.x+self.var+back.valu()+1] = ' '
                matrix[45-Alien.y][Alien.x+self.var+back.valu()+2] = '|'
                matrix[45-Alien.y][Alien.x+self.var+back.valu()+3] = ' '
                matrix[45-Alien.y][Alien.x+self.var+back.valu()+4] = ' '
                matrix[45-Alien.y][Alien.x+self.var+back.valu()+5] = '|'
                matrix[45-Alien.y][Alien.x+self.var+back.valu()+6] = ' '
                matrix[44-Alien.y][Alien.x+self.var+back.valu()+1] = ' '
                matrix[44-Alien.y][Alien.x+self.var+back.valu()+2] = '@'
                matrix[44-Alien.y][Alien.x+self.var+back.valu()+3] = '@'
                matrix[44-Alien.y][Alien.x+self.var+back.valu()+4] = '@'
                matrix[44-Alien.y][Alien.x+self.var+back.valu()+5] = '@'
                matrix[44-Alien.y][Alien.x+self.var+back.valu()+6] = ' '
                matrix[43-Alien.y][Alien.x+self.var+back.valu()+1] = ' '
                matrix[43-Alien.y][Alien.x+self.var+back.valu()+2] = ' '
                matrix[43-Alien.y][Alien.x+self.var+back.valu()+3] = '@'
                matrix[43-Alien.y][Alien.x+self.var+back.valu()+4] = '@'
                matrix[43-Alien.y][Alien.x+self.var+back.valu()+5] = ' '
                return self.var + back.valu()
            except:
                pass
        def delete(self,val):
            try:
                matrix[45-Alien.y][Alien.x+val+1] = ' '
                matrix[45-Alien.y][Alien.x+val+2] = ' '
                matrix[45-Alien.y][Alien.x+val+3] = ' '
                matrix[45-Alien.y][Alien.x+val+4] = ' '
                matrix[45-Alien.y][Alien.x+val+5] = ' '
                matrix[45-Alien.y][Alien.x+val+6] = ' '
                matrix[44-Alien.y][Alien.x+val+1] = ' '
                matrix[44-Alien.y][Alien.x+val+2] = ' '
                matrix[44-Alien.y][Alien.x+val+3] = ' '
                matrix[44-Alien.y][Alien.x+val+4] = ' '
                matrix[44-Alien.y][Alien.x+val+5] = ' '
                matrix[44-Alien.y][Alien.x+val+6] = ' '
                matrix[43-Alien.y][Alien.x+val+1] = ' '
                matrix[43-Alien.y][Alien.x+val+2] = ' '
                matrix[43-Alien.y][Alien.x+val+3] = ' '
                matrix[43-Alien.y][Alien.x+val+4] = ' '
                matrix[43-Alien.y][Alien.x+val+5] = ' '
                matrix[43-Alien.y][Alien.x+val+6] = ' '
            except:
                pass
        def checkbottom(self):
            y=1
            for i in range(2,6):
                if Alien.x+self.var+back.valu()+ 6 > 160 or Alien.x+self.var+back.valu()+ 6 < 0 or matrix[47-Alien.y][Alien.x+self.var+back.valu()+i] != ' ':
                    return 1
            return 0
        def checktop(self):
            y=0
            for i in range(2,6):
                if Alien.x+self.var+back.valu()+ 6 < 160 and Alien.x+self.var+back.valu()+ 6 > 0 and matrix[42-Alien.y][Alien.x+self.var+back.valu()+i] != ' ':
                    y=1
                    break
            if y==1:
                return 1
            else:
                return 0
        def checkleft(self):
            if Alien.x+self.var+back.valu()+1 < 160:
                for i in range(1,4):
                    if Alien.x+self.var+back.valu()+1 > 0 and matrix[42-Alien.y+i][Alien.x+self.var+back.valu()] != ' ':
                        return 1
            return -1
        def checkright(self):
            if Alien.x+self.var+back.valu() +  7 < 160:
                for i in range(1,4):
                    if Alien.x+self.var+back.valu()+12 < 160 and Alien.x+self.var+back.valu()+12 > 0 and matrix[42+i-Alien.y][Alien.x+self.var+back.valu()+7] != ' ':
                        return 1
            return -1

class cloud():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def clprint(self,var):
        try:
            if self.x+var+2 >0:
                matrix[self.y][self.x+var-2]=' '
                matrix[self.y][self.x+var-1] = ' '
                matrix[self.y][self.x+var] = '^'
                matrix[self.y][self.x+var+1] = ' '
                matrix[self.y][self.x+var+2] = ' '
                matrix[self.y+1][self.x+var-2]=' '
                matrix[self.y+1][self.x+var-1] = '^'
                matrix[self.y+1][self.x+var] = '^'
                matrix[self.y+1][self.x+var+1] = '^'
                matrix[self.y+1][self.x+var+2] = ' '
                matrix[self.y+2][self.x+var-3]=' '
                matrix[self.y+2][self.x+var-2]='^'
                matrix[self.y+2][self.x+var-1] = '^'
                matrix[self.y+2][self.x+var] = '^'
                matrix[self.y+2][self.x+var+1] = '^'
                matrix[self.y+2][self.x+var+2] = '^'
                matrix[self.y+2][self.x+var+3] = ' '
                matrix[self.y+3][self.x+var-4]=' '
                matrix[self.y+3][self.x+var-3]='^'
                matrix[self.y+3][self.x+var-2]='^'
                matrix[self.y+3][self.x+var-1] = '^'
                matrix[self.y+3][self.x+var] = '^'
                matrix[self.y+3][self.x+var+1] = '^'
                matrix[self.y+3][self.x+var+2] = '^'
                matrix[self.y+3][self.x+var+3] = '^'
                matrix[self.y+3][self.x+var+4] = ' '
        except:
            pass
class pipe:
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
    def piprint(self,var):
        try:
                for i in range(self.y,self.y+self.length):
                    for j in range(1,9):
                        if j==1 or j==8:
                            try:
                                matrix[i][self.x+j+var] = ' '
                            except:
                                pass
                        else:
                            try:
                                if self.x+j+var>0:
                                    matrix[i][self.x+j+var] = '#'
                            except:
                                pass
        except:
            pass
class Tpipe:
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
    def piprint(self,var):
        try:
                for i in range(self.y,self.y+self.length):
                    for j in range(1,9):
                        if j==1 or j==8:
                            try:
                                matrix[i][self.x+j+var] = ' '
                            except:
                                pass
                        else:
                            try:
                                if self.x+j+var>0:
                                    matrix[i][self.x+j+var] = '^'
                            except:
                                pass
        except:
            pass

class Bricks:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def brprint(self,var):
        for i in range(self.y,self.y+2):#31
            for j in range(1,9):
                if j == 1 or j == 8:
                    try:
                        matrix[i][self.x+j+var] = ' '
                    except:
                        pass
                else:
                    try:
                        if array[self.x] == 0  and self.x+j+var>0:
                            matrix[i][self.x+j+var] = '$'
                        elif array[self.x] == 1:
                            matrix[i][self.x+j+var] = ' '
                    except:
                        pass
class Holes():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def hoprint(self,var):
        for i in range(self.y,self.y+5):#41
            for j in range(1,10):
                try:
                    if self.x+j+var > 0:
                        matrix[i][self.x+j+var] = ' '
                except:
                    pass
