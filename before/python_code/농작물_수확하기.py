import sys
sys.stdin = open("input.txt", "rt")

T = int(input()) # 테스트 케이스의 개수
for test_case in range(1, T+1):
    N = int(input()) #농장의 크기
    farm = list()
    for _ in range(N):
        farm.append(list(map(int, input())))

    size = 1
    value = 0
    reverse = False
    for i in range(N):
        start = (N - size) // 2
        count = 0
        while True:
            if count == size:
                break
            value += farm[i][start]
            start += 1
            count += 1
        if size >= N:
            reverse = True
        if reverse:
            size -= 2
        else:
            size += 2

    print("#{} {}".format(test_case, value))



