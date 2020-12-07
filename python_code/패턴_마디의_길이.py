import sys
sys.stdin = open("input.txt", "rt")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    print("#" + str(test_case), end=" ")

    cnt = 0
    for i in range(1, len(string)):
        if string[i] == string[cnt]:
            cnt += 1
        else:
            cnt = 0
    print(len(string) - cnt)