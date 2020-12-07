direction = {'R':'D', 'D':'R'}
def move(x, y, n, dir):
    # 우측으로 한번 갔으면, 좌측으로 가야함.
    # 만약 해당 방향으로 진행했는데, 벗어나는 경우에는 다른 방향으로 진행해야 함.
    if dir == 'R':
        if 0 <= y+1 < n:
            return x, y+1, direction[dir]
        else:
            return x+1, y, dir
    else:
        if 0 <= x+1 < n:
            return x+1, y, direction[dir]
        else:
            return x, y+1, dir

def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]

    x, y = 0, 0

    if horizontal:
        dir = 'R'
    else:
        dir = 'D'

    while True:
        cur_x, cur_y, dir = move(x, y, n, dir)
        if cur_x >= n or cur_y >= n:
            break
        answer[cur_x][cur_y] = answer[x][y] + 1
        x, y = cur_x, cur_y

        left_diag = False
        while True:
            # 좌하향
            cur_x, cur_y = x + 1, y - 1
            if 0 <= cur_x < n and 0 <= cur_y < n:
                left_diag = True
                answer[cur_x][cur_y] = answer[x][y] + 2
                x, y = cur_x, cur_y
            else:
                break

        if not left_diag:
            while True:
                # 우상향
                cur_x, cur_y = x - 1, y + 1
                if 0 <= cur_x < n and 0 <= cur_y < n:
                    answer[cur_x][cur_y] = answer[x][y] + 2
                    x, y = cur_x, cur_y
                else:
                    break


    return answer

# print(solution(4, True))
print(solution(5, False))

