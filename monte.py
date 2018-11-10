#〇×ゲームで互いにランダムに埋めていった場合
import numpy as np
import random
import matplotlib.pyplot as plt


def check_occupy(F, P, x):  #マスxが空なら1、埋まってたら0、全てのマスが埋まってたら2
    if len(F) + len(P) == 9:
        return 2
    elif x in F or x in P:
        return 0
    else:
        return 1

def check_game(F):  #勝敗が決まってたら１、まだなら0
    if 1 in F and 2 in F and 3 in F:
        return 1

    if 4 in F and 5 in F and 6 in F:
        return 1
    
    if 7 in F and 8 in F and 9 in F:
        return 1

    if 1 in F and 4 in F and 7 in F:
        return 1

    if 2 in F and 5 in F and 8 in F:
        return 1

    if 3 in F and 6 in F and 9 in F:
        return 1

    if 1 in F and 5 in F and 9 in F:
        return 1

    if 3 in F and 5 in F and 7 in F:
        return 1
    
    return 0

def play(A, B): #Aのターン、引き分けなら2、勝ちなら1、続くなら0
    while True:
        x = 1 + random.randrange(9)
        c = check_occupy(A, B, x)
        if c == 2:
            return 2
        elif c == 1:
            break

    A.append(x)
    if check_game(A) == 1:
        return 1
    else:
        return 0

F = []  #Fのとったマス配列
P = []  #Fのとったマス配列
WIN = []  #先手が勝ったら1を、それ以外だったら0を入れる
f_win = 0   #先手の勝数
p_win = 0   #後手の小巣
draw = 0    #引き分け数
n = 1000000 #標本数

for i in range(n):  #n回ゲームを行う
    while True:
        k = play(F, P)
        if k == 2:
            WIN.append(0)
            draw += 1
            break
        elif k == 1:
            WIN.append(1)
            f_win += 1
            break
        
        k = play(P, F)
        if k == 2:
            WIN.append(0)
            draw += 1
            break
        elif k == 1:
            p_win += 1
            WIN.append(0)
            break

    F.clear()
    P.clear()


print ("　平均値：" + str(round(np.mean(WIN), 5)))      #先手の平均勝率
print ("標準誤差：" + str(round(np.std(WIN)/np.sqrt(n), 5)))        #先手の勝率の標準誤差
print (f_win)       #先手の勝数（n回中）
print (p_win)       #後手の勝数（n回中）
print (draw)       #引き分けの回数（n回中）
