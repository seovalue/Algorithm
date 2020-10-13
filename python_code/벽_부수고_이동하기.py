import sys, time
sys.stdin = open("input.txt","rt")
start = time.perf_counter()
n, m = map(int, sys.stdin.readline().split())
Map = list()
for _ in range(n):
    temp = sys.stdin.readline().strip()
    temp = list(map(lambda x: int(x), temp))
    Map.append(temp)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    queue = [(0, 0, 1)]
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1

    while queue:
        x, y, breakCount = queue.pop(0)
        if x == n - 1 and y == m - 1:
            return visit[x][y][breakCount]


        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if Map[nx][ny] == 0 and visit[nx][ny][breakCount] == 0:
                    queue.append((nx, ny, breakCount))
                    visit[nx][ny][breakCount] = visit[x][y][breakCount] + 1
                if Map[nx][ny] == 1 and breakCount == 1:  # 벽이고, 벽을 부수지 않은 경우
                    queue.append((nx, ny, 0))
                    visit[nx][ny][0] = visit[x][y][1] + 1
    return -1

print(bfs())
end = time.perf_counter()

print(end-start)
