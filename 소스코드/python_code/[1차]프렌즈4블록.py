def check(boardInfo, x, y):
    value = boardInfo[x][y][0]
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            if value != boardInfo[i][j][0]:
                return False
    return True


def update(erase, boardInfo, x, y):
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            boardInfo[i][j][1] = 1
            erase.add((i, j))


def move(m, n, boardInfo):
    t = []
    for i in range(n):
        t.append([j[i] for j in boardInfo])  # 행열 변환

    idx = []
    for i in range(n):
        for j in range(m):
            if t[i][j][1]:
                idx.append((i, j))

    while idx:
        x, y = idx.pop(0)
        t[x].pop(y)
        t[x].insert(0, [0,0])

    b = []
    for j in range(m):
        b.append([i[j] for i in t])
    return b


def solution(m, n, board):
    answer = 0
    boardInfo = []
    # board 초기화
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append([board[i][j], 0])
        boardInfo.append(temp)

    erase = set()
    while True:
        flag = False
        for i in range(m):
            for j in range(n):
                if boardInfo[i][j][0] == 0:
                    continue
                if i == m-1 or j == n-1:
                    continue
                if check(boardInfo, i, j):  # 2x2가 모두 같으면
                    update(erase, boardInfo, i, j)
                    flag = True

        answer += len(erase)
        erase = set()
        if flag:
            # 행방향으로 돌면서 한칸씩 내려줌.
            boardInfo = move(m, n, boardInfo)
        else:
            break

    return answer

print(solution(6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))