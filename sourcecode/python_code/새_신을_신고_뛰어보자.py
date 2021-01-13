import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def dfs(matrix, visit, i, j):
    if i == n - 1 and j == n - 1:  # 끝 지점에 도달했다면
        global answer
        answer += 1
    else:
        for k in range(4):
            x = i + matrix[i][j] * dx[k]
            y = j + matrix[i][j] * dy[k]

            if 0 <= x < n and 0 <= y < n and not visit[x][y]:
                visit[x][y] = 1
                dfs(matrix, visit, x, y)
                visit[x][y] = 0


n = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
if matrix[0][0] >= n:
    print(0)
    exit()

visit = [[0] * n for _ in range(n)]
visit[0][0] = 1
dfs(matrix, visit, 0, 0)
print(answer)
