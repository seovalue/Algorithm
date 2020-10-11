import sys
sys.stdin = open("input.txt","r")
def isBingo():

    res = 0
    # 가로 확인
    for i in range(5):
        flag = True
        if 0 in check[i]:
            flag = False
        if flag:
            res += 1

    # 세로 확인
    check_T = list(map(list,zip(*check)))
    for i in range(5):
        flag = True
        if 0 in check_T[i]:
            flag = False
        if flag:
            res += 1


    # 대각선
    r_flag, l_flag = True, True
    for i in range(5):
        if check[i][i] == 0:
            r_flag = False
        if check[i][4-i] == 0:
            l_flag = False
    if r_flag:
        res += 1
    if l_flag:
        res += 1

    if res >= 3:
        return True
    return False


bingo = list()
numbers = list()
check = [[0] * 5 for _ in range(5)]
count = 0

for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))
for _ in range(5):
    numbers.append(list(map(int, sys.stdin.readline().split())))

for number in numbers:
    while number:
        num = number.pop(0)
        count += 1

        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num:
                    check[i][j] = 1
                    i = 5
                    break

        if count >= 5:
            if isBingo() == True:
                print(count)
                exit()
