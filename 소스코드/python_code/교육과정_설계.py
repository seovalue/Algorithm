import sys
sys.stdin = open("input.txt","rt")
from collections import deque

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need) #선수과목으로 초기화
    for x in plan:
        if x in dq: #과목이 선수과목 안에 들어있다면
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))






