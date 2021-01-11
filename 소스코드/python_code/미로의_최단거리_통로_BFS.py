import sys
from collections import deque
sys.stdin = open("input.txt","r")

a = [list(map(int, input().split())) for _ in range(7)]
q = deque()
ch = [[0] * 7 for _ in range(7)]
q.append((0,0))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    tmp = q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and a[x][y] == 0:
            a[x][y] = 1
            ch[x][y] = ch[tmp[0]][tmp[1]]+1 #이전거에 더함=> 거리길이를 구하기 위해서
            q.append((x,y))

if ch[6][6] == 0:
    print(-1)

print(ch[6][6])
