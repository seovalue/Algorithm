import sys
import heapq as hq
sys.stdin = open("input.txt","rt")
a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappush(a)) #a에서 루트노드를 pop 시켜 줌.
    else:
        hq.heappush(a, n) #최소 힙의 형태로 넣는다.