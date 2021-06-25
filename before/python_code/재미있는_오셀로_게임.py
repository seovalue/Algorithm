import sys
sys.stdin = open("input.txt", "rt")
T = int(input())

def init(board, n):
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2
    return board


delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
for test_case in range(1,T+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    # 입력받기

    board = init(board, n)

    for i in range(m):
        x, y, dol = map(int, input().split())
        y, x = y - 1, x - 1

        reverse = []  # 뒤집어야 할 돌을 저장할 리스트 reverse 초기화

        # 8방향 탐색
        for i in range(8):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:  # 모서리인가?
                    reverse = []
                    break
                if board[nx][ny] == 0:  # 빈 칸을 만난경우 reverse를 초기화
                    reverse = []
                    break
                if board[nx][ny] == dol:  # 같은 색을 만났으므로 break
                    break
                else:  # 조건에 부합하는 돌을 reverse에 추가한다.
                    reverse.append((nx, ny))
                nx, ny = nx + dx, ny + dy

            for rx, ry in reverse:
                if dol == 1:
                    board[rx][ry] = 1
                else:
                    board[rx][ry] = 2
        board[x][y] = dol

    black, white = 0, 0
    for b in board:
        black += b.count(1)
        white += b.count(2)

    print("#{} {} {}".format(test_case, black, white))