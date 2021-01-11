dx = [0, 1]
dy = [1, 0]
answer = 0

def dfs(x, y, n, m, visit, matrix):
    global answer
    if x == n - 1 and y == m - 1:
        answer += 1
        return
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and matrix[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, n, m, visit, matrix)
            visit[nx][ny] = 0


def solution(m, n, puddles):
    matrix = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]  # 방문한 곳 표시
    matrix[0][0] = 1  # 집 위치 마킹

    # 웅덩이 위치 마킹
    while puddles:
        a, b = puddles.pop()
        matrix[b - 1][a - 1] = 1

    dfs(0,0,n,m,visit,matrix)
    return answer % 1000000007


def solution(m, n, puddles):
    answer = [[0] * (m + 1) for _ in range(n + 1)]  # 정답 배열
    answer[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue  # 집이 있는 위치
            if [j, i] in puddles:
                answer[i][j] = 0
            else:
                answer[i][j] = (answer[i - 1][j] + answer[i][j - 1]) % 1000000007
    return answer[n][m]