import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
dy = [0] * (n+1)
dy[1] = 1
res = 0
for i in range(2, n+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if a[j] < a[i] and dy[j] > max_val:
            max_val = dy[j]
    dy[i] = max_val + 1
    if dy[i] > res:
        res = dy[i]

print(res)