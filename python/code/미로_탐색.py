import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("input.txt","rt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]


n,m = [int(x) for x in sys.stdin.readline().split()]
answer = n*m + 1
visit = [[0] * m for _ in range(n)]
visit[0][0] = 1
miro = [list(sys.stdin.readline().strip()) for _ in range(n)]

q = []
q.append((0,0))
while q:
    x, y = q.pop(0)
    if x == n-1 and y == m-1:
        print(visit[x][y])
        sys.exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == 0 and miro[nx][ny] == '1':
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
