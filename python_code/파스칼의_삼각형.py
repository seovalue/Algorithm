import sys

sys.stdin = open("input.txt", "rt")

T = int(input())
for test_case in range(1, T + 1):
    print("#" + str(test_case))
    N = int(input())
    pascal = [[1 for _ in range(i)] for i in range(1, N + 1)]
    for i in range(2, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    for p in pascal:
        print(' '.join(map(str,p)))
