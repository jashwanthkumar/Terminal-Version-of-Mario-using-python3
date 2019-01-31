import sys
import os
from colorama import *
from background import *
from Matrix import *
from alien import *
count = 0
past = 0
def printb():
    global Health
    global count
    global post
    os.system('tput reset')
    count += 1
    for i in range(0,160):
        matrix[0][i] = "_"
        matrix[46][i] = "*"
    for i in range(1,46):
        matrix[i][0] = "|"
        matrix[i][159] = "|"
    for i in range(41,46):
        for j in range(1,159):
            matrix[i][j] = '*'

    bck = Background()
    for h in hols:
        h.hoprint(holes())
    '''for i in range(33,41):
        for j in range(1,9):
            if j==1 or j==8:
                try:
                    matrix[i][j+pipes()] = ' '
                except:
                    pass
            else:
                try:
                    if j+pipes()>0:
                        matrix[i][j+pipes()] = '#'
                except:
                    pass'''
    for i in range(31,33):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks1()] = ' '
                except:
                    pass
            else:
                try:
                    if array[0] == 0  and j+bricks1()>0:
                        matrix[i][j+bricks1()] = '$'
                    elif array[0] == 1:
                        matrix[i][j+bricks1()] = ' '
                except:
                    pass
    for i in range(31,33):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks2()] = ' '
                except:
                    pass
            else:
                try:
                    if array[1] == 0  and j+bricks2()>0:
                        matrix[i][j+bricks2()] = '$'
                    elif array[1] == 1:
                        matrix[i][j+bricks2()] = ' '
                except:
                    pass
    for i in range(31,33):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks3()] = ' '
                except:
                    pass
            else:
                try:
                    if array[2] == 0  and j+bricks3()>0:
                        matrix[i][j+bricks3()] = '$'
                    elif array[2] == 1:
                        matrix[i][j+bricks3()] = ' '
                except:
                    pass
    for i in range(31,33):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks4()] = ' '
                except:
                    pass
            else:
                try:
                    if array[3] == 0  and j+bricks4()>0:
                        matrix[i][j+bricks4()] = '$'
                    elif array[3] == 1:
                        matrix[i][j+bricks4()] = ' '
                except:
                    pass
    for i in range(28,30):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks5()] = ' '
                except:
                    pass
            else:
                try:
                    if array[4] == 0  and j+bricks5()>0:
                        matrix[i][j+bricks5()] = '$'
                    elif array[4] == 1:
                        matrix[i][j+bricks5()] = ' '
                except:
                    pass
    for i in range(28,30):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks6()] = ' '
                except:
                    pass
            else:
                try:
                    if array[5] == 0  and j+bricks6()>0:
                        matrix[i][j+bricks6()] = '$'
                    elif array[5] == 1:
                        matrix[i][j+bricks6()] = ' '
                except:
                    pass
    for i in range(33,35):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks7()] = ' '
                except:
                    pass
            else:
                try:
                    if array[6] == 0  and j+bricks7()>0:
                        matrix[i][j+bricks7()] = '$'
                    elif array[6] == 1:
                        matrix[i][j+bricks7()] = ' '
                except:
                    pass
    for i in range(33,35):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks8()] = ' '
                except:
                    pass
            else:
                try:
                    if array[7] == 0  and j+bricks8()>0:
                        matrix[i][j+bricks8()] = '$'
                    elif array[7] == 1:
                        matrix[i][j+bricks8()] = ' '
                except:
                    pass
    for i in range(33,35):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks9()] = ' '
                except:
                    pass
            else:
                try:
                    if array[8] == 0  and j+bricks9()>0:
                        matrix[i][j+bricks9()] = '$'
                    elif array[8] == 1:
                        matrix[i][j+bricks9()] = ' '
                except:
                    pass
    for i in range(26,28):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks10()] = ' '
                except:
                    pass
            else:
                try:
                    if array[9] == 0  and j+bricks10()>0:
                        matrix[i][j+bricks10()] = '$'
                    elif array[9] == 1:
                        matrix[i][j+bricks10()] = ' '
                except:
                    pass
    for i in range(26,28):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks11()] = ' '
                except:
                    pass
            else:
                try:
                    if array[10] == 0  and j+bricks11()>0:
                        matrix[i][j+bricks11()] = '$'
                    elif array[10] == 1:
                        matrix[i][j+bricks11()] = ' '
                except:
                    pass
    for i in range(26,28):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks12()] = ' '
                except:
                    pass
            else:
                try:
                    if array[11] == 0  and j+bricks12()>0:
                        matrix[i][j+bricks12()] = '$'
                    elif array[11] == 1:
                        matrix[i][j+bricks12()] = ' '
                except:
                    pass
    for i in range(26,28):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks13()] = ' '
                except:
                    pass
            else:
                try:
                    if array[12] == 0  and j+bricks13()>0:
                        matrix[i][j+bricks13()] = '$'
                    elif array[12] == 1:
                        matrix[i][j+bricks13()] = ' '
                except:
                    pass
    for i in range(26,28):
        for j in range(1,9):
            if j == 1 or j == 8:
                try:
                    matrix[i][j+bricks14()] = ' '
                except:
                    pass
            else:
                try:
                    if array[13] == 0  and j+bricks14()>0:
                        matrix[i][j+bricks14()] = '$'
                    elif array[13] == 1:
                        matrix[i][j+bricks14()] = ' '
                except:
                    pass
    for t in tpis:
        t.piprint(tpipes())
    for c in clouds:
        c.clprint(bck.valu())
    for  p in pis:
        p.piprint(pipes())

    for i in range(0,47):
        for j in range(0,160):
            if matrix[i][j] == '*':
                print(Fore.RED + matrix[i][j],end='')
            elif matrix[i][j] == '^':
                print(Fore.BLUE + matrix[i][j],end="")
            elif matrix[i][j] == '$':
                print(Fore.YELLOW + matrix[i][j],end="")
            else:
                print(Fore.GREEN + matrix[i][j],end="")
        print("")
    print(Fore.WHITE + "Health : " + str(health()) + "\t" +"Lives : "+ str(lives()) + "\t" +"Score : "+str(score())+"\t"+'press "q" to exit' )
