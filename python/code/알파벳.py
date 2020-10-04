import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**5)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    global answer
    q = set([(x,y,board[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and (board[nx][ny] not in ans):
                q.add((nx,ny,ans+board[nx][ny]))
                answer = max(answer, len(ans)+1)



def dfs(x,y,cnt):
    global passing, answer

    answer = max(cnt, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and (board[nx][ny] not in passing):
            passing.append(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            passing.remove(board[nx][ny])



R, C = map(int, sys.stdin.readline().split())
board = list()
for _ in range(R):
    board.append(list(sys.stdin.readline().split().pop()))
passing = list()
passing.append(board[0][0])
answer = 1
# dfs(0,0,1)
bfs(0,0)
print(answer)


