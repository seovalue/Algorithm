import sys
input = sys.stdin

# 나이트가 이동할 수 있는 칸
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(start, end, visit, l):
    q = [(start[0], start[1])]

    cnt = 0
    while q:
        x, y = q.pop(0)
        if [x, y] == end:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))


t = int(input.readline().strip())
for _ in range(t):
    l = int(input.readline().strip())
    start = list(map(int,input.readline().split()))
    end = list(map(int,input.readline().split()))

    if start == end:
        print(0)
        continue

    visit = [[0] * l for _ in range(l)]
    visit[start[0]][start[1]] = 1
    bfs(start, end, visit, l)
    print(visit[end[0]][end[1]] - 1)


