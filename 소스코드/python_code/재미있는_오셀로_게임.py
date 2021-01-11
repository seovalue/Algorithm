import sys
sys.stdin = open("input.txt", "rt")

# 보드 초기화
def init(board, n):
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2
    return board

# 사이에 돌이 있는지 확인한다.
# w를 만났을 때 좌표와 방향을 저장한 뒤, B를 만난다면 w를 바꾸고
dx = [-2, -2, -2, 0, 0, 2, 2, 2]
dy = [-2, 0, 2, -2, 2, -2, 0, 2]
def put_and_change(x, y, dol, board, n):
    board[x][y] = dol
    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and board[nx][ny] == dol:
            board[(x + nx) // 2][(y + ny) // 2] = dol # 돌 잡아 먹기
    return board

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())  # n은 한 변의 길이, m은 플레이어가 돌을 놓는 횟수
    board = [[0] * n for _ in range(n)]
    board = init(board, n)
    print(board)
    for _ in range(m):
        y, x, dol = map(int, input().split())
        board = put_and_change(x-1, y-1, dol, board, n)
    print(board)
    black, white = 0, 0
    for b in board:
        black += b.count(1)
        white += b.count(2)

    print("#{} {} {}".format(test_case, black, white))


# 다시 풀어보귀!!!!!