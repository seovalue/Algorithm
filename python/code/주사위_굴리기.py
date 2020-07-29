import sys
sys.stdin = open("input.txt","rt")
n,m,x,y,k = map(int,input().split())

def checkDir(cmd):
    dir = []
    if cmd == 1:
        dir = [0,1]
    elif cmd == 2:
        dir = [0,-1]
    elif cmd == 3:
        dir = [-1,0]
    else:
        dir = [1,0]
    return dir

def diceNow(cmd):
    if cmd == 1:
        dice[1],dice[3],dice[4],dice[6]=dice[3], dice[6],dice[1],dice[4]
    elif cmd == 2:
        dice[1],dice[3],dice[4],dice[6]=dice[4],dice[1],dice[6],dice[3]
    elif cmd==3:
        dice[1],dice[2],dice[5],dice[6]=dice[2], dice[6], dice[1], dice[5]
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
matrix = list()
for i in range(n):
    matrix.append(list(map(int,input().split())))
cmdList = list(map(int,input().split()))

dice = [0] * 7
dice_now = 0
while cmdList:
    cmd = cmdList.pop(0)
    dir = checkDir(cmd)
    x = x + dir[0]
    y = y + dir[1]

    if 0 <= x < n and 0 <= y < m:
        diceNow(cmd)
        if matrix[x][y] != 0:
            dice[1] = matrix[x][y]
            matrix[x][y] = 0

    print(dice[6]) #윗면

