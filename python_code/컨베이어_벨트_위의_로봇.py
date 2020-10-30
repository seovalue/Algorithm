import sys, collections
input = sys.stdin

def move_belt(up, down):
    up -= 1
    down -= 1

    if up < 0:
        up = n * 2 - 1
    if down < 0:
        down = n * 2 -1
    return up, down

def move_robot(robot, down):
    global robot_visited
    size = len(robot)
    for i in range(size):
        cur = robot[0]
        robot_visited[cur] = 0
        robot.pop(0)

        # 로봇이 내려가는 위치에 있으면
        if cur == down:
            continue

        # 그 다음 위치를 정하고,
        if cur + 1 <= n * 2 - 1:
            next = cur + 1
        else:
            next = 0

        # 다음 위치의 벨트의 내구도가 1 이상이고 로봇이 없다면
        if belt[next] >= 1 and robot_visited[next] == 0:
            belt[next] -= 1
            if next == down: continue
            robot_visited[next] = 1
            robot.append(next)
        else: #움직이지 않고 가만히 있는 경우
            robot_visited[cur] = 1
            robot.append(cur)

    return robot

def make_robot(up, down, robot_visited, robot_on):
    if robot_visited[up] == 0 and belt[up] >= 1:
        robot_visited[up] = 1
        belt[up] -= 1
        robot_on.append(up)


n, k = map(int, input.readline().split())
belt = list(map(int, input.readline().split())) #내구도
robot_visited = [0] * n * 2 #로봇이 위치해있으면 1
robot = []
up, down = 0, n-1
answer = 0

while True:
    answer += 1
    # 벨트를 한칸 움직인다.
    up, down = move_belt(up, down)

    # 로봇을 한 칸 움직인다.
    if robot: #로봇이 있으면
        robot = move_robot(robot, down)
    make_robot(up,down,robot_visited, robot)

    if belt.count(0) >= k:
        print(answer)
        break













