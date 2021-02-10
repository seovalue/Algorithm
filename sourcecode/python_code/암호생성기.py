'''
1225번, 알고리즘 스터디
'''
import sys

sys.stdin = open("input.txt", "rt")


def logic(numbers):
    minus = 1
    while True:
        number = numbers.pop(0)
        if number - minus <= 0:
            numbers.append(0)
            break
        numbers.append(number - minus)
        minus += 1

        if minus > 5: # 한 사이클
            minus = 1
    return numbers


def print_list(test_case, numbers):
    print("#{}".format(test_case), end = " ")
    for number in numbers:
        print(number, end=" ")
    print()


for _ in range(10):
    test_case = int(input())
    numbers = list(map(int, input().split()))
    numbers = logic(numbers)
    print_list(test_case, numbers)
