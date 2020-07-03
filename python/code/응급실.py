import sys
from collections import deque
sys.stdin = open("input.txt","rt")

n, m = map(int,input().split())
danger = [(pos,val) for pos, val in enumerate(list(map(int, input().split())))]
danger = deque(danger)
cnt = 0

while True:
    cur = danger.popleft()
    if all(cur[1] > x[1] for x in danger):
        danger.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
