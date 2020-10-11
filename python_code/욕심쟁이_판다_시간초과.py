import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open("input.txt","rt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            if check[nx][ny] == 1 or check[x][y] + 1 > check[nx][ny]:
                check[nx][ny] = check[x][y] + 1
                dfs(nx, ny)


n = int(sys.stdin.readline())
forest = []
for _ in range(n):
    forest.append(list(map(int,sys.stdin.readline().split())))

check = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if check[i][j] == 1:
            dfs(i,j)

res = 0
for i in range(n):
    comp = max(check[i])
    res = comp if res < comp else res

print(res)