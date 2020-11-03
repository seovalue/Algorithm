# 대각선 아래로 한칸 오른쪽, 한칸 왼쪽
dx = [1,1]
dy = [0,1]
answer = 0
def dfs(matrix, visit, height, x, y, total):
    if x == height - 1: #마지막 노드에 도달했을 때
        global answer
        total += matrix[x][y]
        answer = total if total > answer else answer #더 큰 값으로 업데이트
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < height and matrix[nx][ny] != -1 and not visit[nx][ny]:
                visit[nx][ny] = 1
                dfs(matrix, visit, height, nx, ny, total+matrix[x][y])
                visit[nx][ny] = 0


def solution(triangle):
    height = len(triangle)

    triangle_matrix = []
    for t in triangle:
        size = height - len(t) #추가해야할 -1의 개수
        for _ in range(size):
            t.append(-1)
        triangle_matrix.append(t)
    visit = [[0] * height for _ in range(height)]
    visit[0][0] = 1
    dfs(triangle_matrix, visit, height, 0, 0, 0)
    return answer

print(solution([[1],[2,3],[4,5,6]])) #30