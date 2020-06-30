#import sys
#sys.stdin = open("input.txt","rt")

N = int(input())
scoring = list(map(int, input().split()))

cnt = 1
total = 0
for score in scoring:
    if score == 1:
        total += cnt * 1
        cnt += 1
    elif score == 0:
        cnt = 1

print(total)