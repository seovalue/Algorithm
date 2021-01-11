directions = {'U':[-1,0], 'D':[1,0], 'R':[0,1], 'L':[0,-1]}

def set(dir):
    if dir == 'U':
        return 'D'
    if dir == 'D':
        return 'U'
    if dir == 'R':
        return 'L'
    if dir == 'L':
        return 'R'


def solution(dirs):
    answer = 0
    plane = [[0] * 11 for _ in range(11)] #평면
    visit = [[[0,'']] * 11 for _ in range(11)]
    i, j = 5, 5 #시작점
    visit[i][j] = [1,set(dirs[0])] #시작점 표시, 어느 방향에서 들어왔는지까지

    for d in dirs:
        x, y = directions[d] #방향 표시
        nx, ny = i + x, j + y
        if 0 <= nx < 11 and 0 <= ny < 11:
            if visit[nx][ny][0] == 0: #방문하지 않은 곳이라면
                visit[nx][ny] = [1, d]
                answer += 1
            elif visit[nx][ny][0] == 1: #이미 방문한 곳인데,
                if d not in visit[nx][ny][1]: #해당 방향으로는 들어오지 않았다면
                    visit[nx][ny][1] += d
                    answer += 1
            i, j = nx, ny

    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UDUD"))
print(solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU"))
print(solution("ULDDRU"))
