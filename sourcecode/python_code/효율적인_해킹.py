import sys
input = sys.stdin
input = open("input.txt","rt")

n, m = map(int,input.readline().split())
board = [[0] * (n+1) for _ in range(n+1)]
computers = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input.readline().split())
    board[b][a] = 1 #a는 b를 신뢰한다 -> b의 신뢰자는 a임을 1로 나타낸다.
    computers[b] += 1 #b에 연결된 신뢰 컴퓨터의 수
    for i in range(n+1):
        if board[i][b] == 1: #b가 신뢰하는 컴퓨터인가?
            computers[i] += computers[b]

top = max(computers)
for i in range(len(computers)):
    if top <= computers[i]:
        print(i, end=' ')