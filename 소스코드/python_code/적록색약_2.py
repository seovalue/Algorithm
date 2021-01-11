import sys
input = sys.stdin


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j, grid, visit, N, color):
    q = [(i, j)]
    visit[i][j] = 1
    while q:
        x, y = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and grid[nx][ny] in color:
                visit[nx][ny] = 1
                q.append((nx,ny))

def count(flag):
    visit = [[0] * N for _ in range(N)]
    answer = {'R': 0, 'G': 0, 'B': 0}

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if flag and (grid[i][j] == 'G' or grid[i][j] == 'R'):
                    bfs(i, j, grid, visit, N, ['G','R'])
                else:
                    bfs(i,j,grid,visit,N,grid[i][j])
                answer[grid[i][j]] += 1
    return answer

N = int(input.readline().strip())
grid = [list(input.readline().strip()) for _ in range(N)]
print(sum(list(count(0).values())))
print(sum(list(count(1).values())))

