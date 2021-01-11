import sys

sys.stdin = open("input.txt", "rt")

T = int(sys.stdin.readline().strip())
for test_case in range(T):
    N = sys.stdin.readline().strip()
    price = list(map(int, sys.stdin.readline().split()))
    money = 0

    start_index = 0
    while price:
        max_index = price.index(max(price))
        cnt = 0
        for i in range(start_index, max_index):
            cnt += 1
            money -= price[i]
        money += price[max_index] * cnt
        price = price[max_index + 1:]

    print("#"+str(test_case), end=" ")
    print(money)

