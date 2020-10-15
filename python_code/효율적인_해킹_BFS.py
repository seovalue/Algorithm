import sys, collections
input = sys.stdin
input = open("input.txt","rt")

def bfs(idx):
    q = collections.deque()
    q.append(idx)
    visit = [0] * (n+1)
    cnt = 1
    while q:
        i = q.popleft()
        for j in board[i]:
            if not visit[j]: #아직 방문하지 않았다면
                q.append(j)
                visit[j] = 1
                cnt += 1
    return cnt




n, m = map(int,input.readline().split())
board = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input.readline().split())
    board[b].append(a)

cnt = [0]
for i in range(1, n+1):
    cnt.append(bfs(i))

top = max(cnt)
for i in range(len(cnt)):
    if cnt[i] >= top:
        print(i, end = ' ')
