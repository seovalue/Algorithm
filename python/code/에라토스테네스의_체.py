import sys
sys.stdin = open("input.txt")
n, k = map(int, sys.stdin.readline().split())

numbers = [i for i in range(2, n+1)]
visit = [0] * (n-1)
for number in numbers:
    for idx, num in enumerate(numbers):
        if num >= number and num % number == 0 and visit[idx] != 1:
            visit[idx] = 1
            k -= 1
        if k == 0:
            print(num)
            exit()

