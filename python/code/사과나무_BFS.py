import sys
from collections import deque
sys.stdin = open("input.txt","r")

dx = [-1,0,1,0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]* n for _ in range(n)]
total = 0
q= deque()
ch[n//2][n//2] = 1
total += a[n//2][n//2]
q.append((n//2,n//2))
L = 0
while True:
    if L == n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        for j in range(4): #상하좌우
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                total += a[x][y]
                ch[x][y] = 1
                q.append((x,y))
    L+=1

print(total)

'''
n = int(input())
mat = list()
for i in range(n):
    inputMat = list(map(int,input().split()))
    mat.append(inputMat)

count = 1
total = 0
flag = False
for i in range(n):
    idx = (n-count) // 2
    for j in range(idx,idx+count):
        total += mat[i][j]

    if i < (n//2):
        count += 2
    else:
        count -= 2

print(total)
'''