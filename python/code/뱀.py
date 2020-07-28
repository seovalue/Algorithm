import sys
import math
sys.stdin = open("input.txt","rt")
def R(x):
    return [[round(math.cos(x)), -round((math.sin(x)))],[round(math.sin(x)), round(math.cos(x))]]

def Rotation(str, d):
    result = []
    if str == 'L': #left
        rMatrix = R(math.radians(90))
    elif str == 'D': #right
        rMatrix = R(math.radians(-90))

    for i in range(len(rMatrix)):
        tmpVal = 0
        for j in range(len(rMatrix[0])):
            tmpVal += rMatrix[i][j] * d[j]
        result.append(tmpVal)

    return result

n = int(input()) #보드의 크기
board = [[0] * n for _ in range(n)]
snake = [[0] * n for _ in range(n)]
snake[0][0] = 1

k = int(input()) #사과의 개수 K
for _ in range(k):
    apple = list(map(int,input().split()))
    board[apple[0]-1][apple[1]-1] = 1 #사과가 있는 자리는 1로 표시

l = int(input())
going = list()
for _ in range(l):
    going.append(list(input().split()))

time,rotation = going.pop(0)
time = int(time)

#뱀의 머리(이동)
x = 0
y = 0

dir = [0, 1] #이동하는 방향
second = 1 #시간 초
tail = list() #뱀의 꼬리

while True:
    if second - 1 == time:
        dir = Rotation(rotation, dir)
        if going:
            time, rotation = going.pop(0)
            time = int(time)
        else:
            time = -1
    tail.append([x,y])
    x = x + dir[0]
    y = y + dir[1]
    if (0 > x or n <= x) or (0 > y or n <= y):
        break
    if snake[x][y] == 1: #이미 뱀의 몸이 있는 경우
        break

    if board[x][y] == 0: #사과가 없는 경우
        s_x, s_y = tail.pop(0)
        snake[s_x][s_y] = 0 #꼬리를 한칸 옮김
    else:
        board[x][y] = 0 #사과를 먹었으므로 0으로 바꾸어줌

    snake[x][y] = 1
    second += 1

print(second)

