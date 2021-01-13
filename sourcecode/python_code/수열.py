import sys
sys.stdin = open("input.txt","rt")

n = int(sys.stdin.readline().strip())
seq = list(map(int,sys.stdin.readline().split()))


result = 1
cnt = 1
for i in range(1,n):
    if seq[i-1] <= seq[i]:
        cnt += 1
    else:
        cnt = 1
    result = cnt if cnt > result else result
cnt = 1
for i in range(1, n):
    if seq[i - 1] >= seq[i]:
        cnt += 1
    else:
        cnt = 1
    result = cnt if cnt > result else result

print(result)