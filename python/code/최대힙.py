import sys
import heapq as hq
sys.stdin = open("input.txt","rt")
a = []

#heapq는 최소 힙이므로 최대 힙으로 할 땐 -를 붙이고, 출력할 때 다시 - 를 붙여 +로 만든다.
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)
