import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin

def search(time, pay):
    if time == N+1: #일을 할 수 없는 날이면
        global answer
        answer = max(answer, pay)
        return

    # 오늘 일을 하는 경우
    if time + T[time] <= N+1: #다음번에 일 할 날짜가 N+1보다 작거나 같다면
        search(time + T[time], pay+P[time]) #다시 탐색, pay는 오늘 일한 것만큼 업데이트

    # 오늘 일을 안하는 경우
    if time + 1 <= N+1:
        search(time+1, pay) #다음 날로 다시 탐색, pay는 업데이트 하지 않음.


N = int(input.readline().strip())
T = [0,]
P = [0,]
for _ in range(N):
    t, p = map(int,input.readline().split())
    T.append(t)
    P.append(p)

answer = 0
search(1, 0)
print(answer)



