import sys
sys.setrecursionlimit(10 ** 5)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j, n, type, visit, v):
    q = [(i, j)]

    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == type and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))

def solution(v):
    answer = [0, 0, 0]
    n = len(v)
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                bfs(i,j, n,v[i][j],visit,v)
                answer[v[i][j]] += 1
    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]])) #[2,1,2]
print(solution([[0,0,1],[2,2,1],[0,0,0]])) #[2,1,1]