import sys
sys.stdin = open("input.txt","rt")

board = [list(map(int,input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]: #거꾸로
            cnt += 1
        #세로로는 슬라이스 안됨. 하나의 리스트가 아니므로
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]: #길이 5짜리 회문을 검사하는 것이므로. 0,1과 3,4만 비교함
                break
        else:
            cnt += 1

print(cnt)
