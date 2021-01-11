import sys
sys.stdin = open("input.txt","rt")

n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0: #왼쪽 방향 회전
        for _ in range(k): #k만큼 회전
            mat[h-1].append(mat[h-1].pop(0))
    else: #오른쪽 방향 회전
        for _ in range(k):
            mat[h-1].insert(0,mat[h-1].pop()) #pop(0)은 0번째 자리, pop()하면 맨 뒤 pop

total = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s, e+1):
        total += mat[i][j]
    if i < n//2 : #좁히기
        s += 1
        e -= 1
    else: #넓히기
        s -= 1
        e += 1

print(total)


