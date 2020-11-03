# 대각선 아래로 한칸 오른쪽, 한칸 왼쪽
dx = [1,1]
dy = [0,1]

def bfs(matrix, height, i, j):
    visit = [[0] * height for _ in range(height)]
    visit[0][0] = matrix[0][0]
    q = [(i,j)]

    while q:
        x,y = q.pop(0) #인덱스

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < height and matrix[nx][ny] != -1:
                if not visit[nx][ny]:
                    visit[nx][ny] = matrix[nx][ny] + visit[x][y] #누적합
                    q.append((nx, ny))
                else:
                    visit[nx][ny] = max(matrix[nx][ny] + visit[x][y], visit[nx][ny])
    return max(visit[len(visit)-1])



def solution(triangle):
    height = len(triangle)

    triangle_matrix = []
    for t in triangle:
        size = height - len(t) #추가해야할 -1의 개수
        for _ in range(size):
            t.append(-1)
        triangle_matrix.append(t)

    answer = bfs(triangle_matrix, height, 0, 0)
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) #30
