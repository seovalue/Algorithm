from collections import deque
import sys
sys.stdin = open("input.txt", "rt")
dx = [-1,0,0,1]
dy = [0,-1,1,0]




def bfs(_x,_y):
    q, visited = deque([(_x,_y)]), set([(_x,_y)])
    seconds = 0 # 걸린 초
    baby = 2 # 아기 상어의 크기
    eat = 0 # 현재 크기에서 지금까지 먹은 먹이의 수
    eat_flag = False  # 현재 상태에서 물고기를 먹은 경우, for _ in range(size)를 실행하지 않기 위한 플래그

    answer = 0
    while q:
        size = len(q)
        q = deque(sorted(q))

        for _ in range(size):
            x, y = q.popleft()

            # 현재 자리에서 먹이를 먹는 경우
            if space[x][y] < baby and space[x][y] != 0:
                space[x][y] = 0
                eat += 1

                if eat == baby:
                    baby += 1
                    eat = 0

                q, visited = deque(), set([(x, y)])
                eat_flag = True
                answer = seconds #여기까지 오는 데 까지 걸린 초를 answer 에 업데이트함.

            for _dx, _dy in zip(dx,dy):
                nx, ny = x + _dx, y +_dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if space[nx][ny] <= baby:
                        q.append((nx,ny))
                        visited.add((nx,ny))

            if eat_flag:
                eat_flag = False
                break

        seconds += 1
    return answer

n = int(sys.stdin.readline().strip())
space = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 초기 상어의 위치를 파악하고, 해당 자리를 판에서 비운다.
x,y = None, None
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            x,y = i,j
            space[i][j] = 0
            i = n + 1
            break

# 시작점에서 bfs를 진행한다.
print(bfs(x,y))
