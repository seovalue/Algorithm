import sys
input = sys.stdin

n = int(input.readline().strip())
cnt = 0
loop = n // 5
for i in range(loop, -1, -1):
    if (n - (5 * i)) % 3 == 0:
        cnt += i
        cnt += (n - (5*i)) // 3
        print(cnt)
        exit()
else:
    print(-1)
