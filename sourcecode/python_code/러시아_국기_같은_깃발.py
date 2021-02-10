import sys
sys.stdin = open("input.txt", "rt")
T = int(input()) #테스트케이스
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    before_flag = []
    after_flag = []
    for _ in range(N):
        before_flag.append(input())

    answer = 0
    white, blue, red = 0, 0, 0
    for i in range(N):
        if white:
            break
