from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 보드는 위 아래 좌우가 연결되어있으므로,
# 벗어난 좌표를 올바른 곳으로 이동시킨다.
def move(x, n):
    if x < 0:
        return x + n
    elif x == n:
        return x - n
    return x

def bfs(n, board, i, j, goal):
    q = deque()
    q.append([i,j])
    visit = [[0] * n for _ in range(n)] #방문 표시
    while q:
        x, y = q.popleft()
        if board[x][y] == goal:
            return [x, y, visit[x][y] + 1]

        for i in range(4):
            nx, ny = move(x+dx[i], n), move(y+dy[i], n)
            if visit[nx][ny] == 0:
                visit[nx][ny] += visit[x][y] + 1
                q.append([nx, ny])


def solution(n, board):
    answer = 0
    x, y = 0, 0
    for num in range(1, n**2 + 1):
        x, y, cnt = bfs(n, board, x, y, num)
        answer += cnt

    return answer

print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
print(solution(2, [[2, 3], [4, 1]]))
print(solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]))
print(solution(1,[[1]]))
print(solution(5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))