#import sys
#sys.stdin = open("input.txt","rt")

N = int(input())

MONEY = []
for n in range(N):
    dice = list(map(int,input().split()))

    tmp = 0
    cnt = 1
    same = 0
    for num in dice:
        if tmp == num:
            cnt += 1
            same = num
        tmp = num

    money = 0
    #규칙 1 만족
    if cnt == len(dice):
        money = 10000 + (same * 1000)
    elif cnt == len(dice) -1:
        money = 1000 + (same * 100)
    else:
        money = max(dice)*100

    MONEY.append(money)

print(max(MONEY))
