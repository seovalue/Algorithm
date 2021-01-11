#import sys
#sys.stdin = open("input.txt","rt")

'''
입력을 받음
출발지 (0,0)에서 시작
dx = [-1,0,1,0]
dy = [0,-1,0,1] 
(0,0)에서부터 상하좌우로 이동하면서 해당 좌표의 값이 0이고, 틀을 벗어나지 않은 경우 이동
방문한 경우에는 visit 배열을 1로 바꾸어 준다.
이동 후, 도착 지점 (6,6) 에 도달했을 때 cnt += 1 증가
'''

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def dfs(_x,_y):
    visit[_x][_y] = 1
    global cnt
    if _x == 6 and _y == 6:
        cnt += 1
    else:
        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]
            if 0 <= x < 7 and 0<= y < 7 and visit[x][y] == 0 and mat[x][y] == 0:
                dfs(x,y)
                visit[x][y] = 0

mat = [list(map(int,input().split())) for _ in range(7)]
visit = [[0] * 7 for _ in range(7)]
cnt = 0
dfs(0,0)
print(cnt)