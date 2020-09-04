import sys

sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    if x == 0 and y == 0:
        return 1
    if visit[x][y] == -1:
        visit[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny] > matrix[x][y]:
                    visit[x][y] += dfs(nx,ny)
    return visit[x][y]



n,m = [int(x) for x in sys.stdin.readline().split()]
matrix = list()
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])
visit = [[-1] * m for _ in range(n)]

print(dfs(n-1,m-1))



