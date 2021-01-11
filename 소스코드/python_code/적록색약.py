'''
방문하지 않은 노드이고 색이 같은 노드이면 이동.
상하좌우에 색이 같은 노드가 없으면 중지. 카운트 증가

적록색약
R과 G를 같은 글자로 취급
'''

import sys
sys.stdin = open("input.txt","rt")
sys.setrecursionlimit(100000) #이코드 추가 안하면 백준에서 안돌아감..

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(type, i, j, color, visit):
    global n
    global mat
    global dx, dy

    if visit[i][j] == 0:
        visit[i][j] = 1

    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if type == 0:  # 일반인
            if visit[x][y] == 0 and mat[x][y] == color:
                dfs(0, x, y, color, visit)
        elif type == 1:  # 적록색약
            if color == 'R' or color == 'G':
                if visit[x][y] == 0 and (mat[x][y] == 'G' or mat[x][y] == 'R'):
                    dfs(1, x, y, color, visit)
            else:
                if visit[x][y] == 0 and mat[x][y] == color:
                    dfs(1, x, y, color, visit)


if __name__ == "__main__":
    n = int(input())
    mat = []
    for i in range(n):
        val = list(input())
        mat.append(val)

    visit1 = [[0] * n for _ in range(n)]
    count1 = 0

    for i in range(n):
        for j in range(n):
            if visit1[i][j] == 0:
                dfs(0, i, j, mat[i][j], visit1)
                count1 += 1

    visit2 = [[0] * n for _ in range(n)]
    count2 = 0

    for i in range(n):
        for j in range(n):
            if visit2[i][j] == 0:
                dfs(1, i, j, mat[i][j], visit2)
                count2 += 1

    print("{0} {1}".format(count1, count2))