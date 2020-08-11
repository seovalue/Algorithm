import sys
sys.stdin = open("input.txt","rt")
sys.setrecursionlimit(10**5)

#우,하,좌,상
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

def dfs(st1, st2, x,y, garo, sero):
    i = 0
    while True:
        if x == st1 and y == st2:
            return garo, sero
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if matrix[nx][ny] != 1: i += 1




T = int(input())
n, k = map(int,sys.stdin.readline().split())

matrix = list()
for i in range(n):
    for j in range(n):
        matrix.append(list(map(int,sys.stdin.readline().split())))

visit = [[0] * 10 for _ in range(10)]
