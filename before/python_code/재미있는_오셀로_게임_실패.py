import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10 ** 8)

# 보드 초기화
def init(board, n):
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2
    return board

# 사이에 돌이 있는지 확인한다.
# w를 만났을 때 좌표와 방향을 저장한 뒤, B를 만난다면 w를 바꾸고
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def put(x, y, dol, board, n):
    board[x][y] = dol
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        # 돌이 존재하며, 비교하려는 돌과 색이 다른 돌이 존재하는 경우
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and board[nx][ny] != dol:
            move_forward(nx, ny, board, (dx[i], dy[i]), dol)
            # board[(x + nx) // 2][(y + ny) // 2] = dol # 돌 잡아 먹기
    return board

def move_forward(x, y, board, direction, origin_dol):
    save_location = [(x, y)]
    dx, dy = direction
    while True:
        # 같은 방향으로 이동
        nx, ny = x + dx, y + dy
        # 다른 색을 만나면
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and board[nx][ny] == origin_dol:
            break
        save_location.append((nx, ny))
    change_color(save_location, board, origin_dol)

def change_color(location, board, dol):
    for loc in location:
        x, y = loc
        board[x][y] = dol

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())  # n은 한 변의 길이, m은 플레이어가 돌을 놓는 횟수
    board = [[0] * n for _ in range(n)]
    board = init(board, n)
    for _ in range(m):
        y, x, dol = map(int, input().split())
        board = put(x - 1, y - 1, dol, board, n)
        black, white = 0, 0
        for b in board:
            black += b.count(1)
            white += b.count(2)


    black, white = 0, 0
    for b in board:
        black += b.count(1)
        white += b.count(2)

    print("#{} {} {}".format(test_case, black, white))

# 다시 풀어보귀!!!!!
