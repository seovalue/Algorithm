# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
mt = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
    for j in range(n):
        flag = True
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if ( x >= n or y >= n or x < 0 or y < 0): continue
            if (mt[i][j] <= mt[x][y]):
                    flag = False
        if(flag):
            cnt += 1


'''
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(mt[i][j] > mt[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
'''
print(cnt)