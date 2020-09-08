import sys
import copy
from collections import deque
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt","rt")
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(tomatoes):
    days = -1
    while farm: #익지않은 토마토가 존재하는 동안
        days += 1
        for _ in range(len(farm)):
            x, y = farm.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = tomatoes[x][y] + 1
                    farm.append((nx,ny))
    for tomato in tomatoes:
        if 0 in tomato:
            return -1
    return days

m,n = map(int,sys.stdin.readline().split())
tomatoes = list()
for _ in range(n):
    tomatoes.append(list(map(int,sys.stdin.readline().split())))

farm = deque()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            farm.append((i,j)) #farm에 익은 토마토의 위치를 넣어준다.

print(bfs(tomatoes))



