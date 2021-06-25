n = int(input())
a = list(map(int, input().split()))
dy = [0] * n
dy[0] = 1
length = 0

for i in range(1, n):
    max_val = 0
    for j in range(i):
        if a[j] < a[i] and dy[j] > max_val:
            max_val = dy[j]
    dy[i] = max_val + 1

print(max(dy))