import sys
import itertools

n = 4

direction = {'D':'R','R':'U','U':'D'} #아래다음은 오른쪽, 오른다음은 위쪽, 위다음은 아래쪽

def get_direction(d):
    if d == 'D':
        return 1,0
    elif d == 'R':
        return 0, 1
    else:
        return -1, -1

def solution(n):
    answer = []
    max_num = sum(range(1,n+1))
    snail = [[0] * i for i in range(1,n+1)]
    x, y, dir = 0,0,'D'

    num = 1
    while num <= max_num:
        snail[x][y]= num

        dx, dy = get_direction(dir)
        nx, ny = x + dx, y+dy
        if (nx < 0 or nx >= n) or (ny > nx) or snail[nx][ny] != 0: #방향을 바꾸어야 함.
            dir = direction[dir] #진행 방향 번경
            dx, dy = get_direction(dir)
            nx, ny = x + dx, y + dy
        x, y = nx, ny
        num += 1


    answer = list(itertools.chain(*snail))
    return answer


print(solution(5))

