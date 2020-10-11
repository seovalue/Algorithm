# import sys
# sys.stdin = open("input.txt",'rt')

n = int(input())
numbers = list(map(int,input().split()))


def digit_sum(x):
    result = 0
    while(x > 0):
        result += (x % 10)
        x = int(x / 10)
    return result

maxdigit = 0
maxNum = 0
for number in numbers:
    tmp = digit_sum(number)
    if(maxdigit < tmp):
        maxdigit = tmp
        maxNum = number

print(maxNum)