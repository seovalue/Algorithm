import sys
sys.stdin = open("input.txt","rt")

def getPalindrome(li):
    size = len(li)
    for i in range(size):
        if li[i] != li[size-1-i]:
            return False
    return True

for test_case in range(1,11):
    n = int(input())
    board = list()
    for _ in range(8):
        board.append(list(input()))

    cnt = 0

    #가로 확인
    for i in range(8):
        for j in range(8):
            if j+n <= 8:
                garo = board[i][j:j+n]
                if getPalindrome(garo) == True:
                    cnt += 1
            else:
                break

    #세로 확인
    for i in range(8):
        List = [j[i] for j in board]
        for k in range(8):
            if k+n <= 8:
                sero = List[k:k+n]
                if getPalindrome(sero) == True:
                    cnt += 1
            else:
                break


    print("#%d %d" %(test_case,cnt))
