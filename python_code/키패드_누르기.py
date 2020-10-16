'''
키패드를 배열로 저장한다.
거리를 구할 때에는 bfs를 사용하여 최단 거리를 구한다.
'''
import collections

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, "#"]]
m, n = 4, 3
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def get_distance(a, b, goal):
    # a,b는 시작점, goal은 목표 번호
    q = collections.deque()
    q.append((a, b))
    visit = [[0] * 3 for _ in range(4)]
    visit[a][b] = 1
    answer = []
    while q:
        x, y = q.popleft()
        if keypad[x][y] == goal:
            answer = [x, y]
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] += visit[x][y] + 1
    return visit[answer[0]][answer[1]] - 1


# 좌표를 구하는 함수
def get_loc(num):
    for i in range(m):
        if num in keypad[i]:
            return [i, keypad[i].index(num)]


def solution(numbers, hand):
    answer = ''
    only_left = [1, 4, 7]  # 왼손만 가능
    only_right = [3, 6, 9]  # 오른손만 가능

    # 각 손 위치의 첫 좌표 (#, *)
    hands = {"right": [3, 2], "left": [3, 0]}

    for i in range(len(numbers)):
        number = numbers[i]

        # 처음인데 중간인 경우
        if i == 0 and (number not in only_left) and (number not in only_right):
            if hand == "right":
                answer += 'R'
            else:
                answer += 'L'
            hands[hand] = get_loc(number)
            continue

        # 왼손이 치는 경우에 속할 때
        if number in only_left:
            answer += 'L'
            hands['left'] = get_loc(number)
        elif number in only_right:
            # 오른손이 치는 경우에 속할 때
            answer += 'R'
            hands['right'] = get_loc(number)
        else:
            # 중간(거리를 구해야하는 경우)
            r_x, r_y = hands['right']
            dist_r = get_distance(r_x, r_y, number)

            l_x, l_y = hands['left']
            dist_l = get_distance(l_x, l_y, number)

            if dist_r < dist_l:
                answer += 'R'
                hands['right'] = get_loc(number)
            elif dist_l < dist_r:
                answer += 'L'
                hands['left'] = get_loc(number)
            else:
                if hand == "right":
                    answer += 'R'
                else:
                    answer += 'L'
                hands[hand] = get_loc(number)

    return answer