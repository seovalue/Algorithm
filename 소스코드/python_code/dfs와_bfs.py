import sys, collections
sys.setrecursionlimit(10 ** 5)
sys.stdin = open("input.txt","rt")

def dfs(x):
    visit[x] = 1
    print(x+1, end=' ')
    for i in range(n):
        if graph[x][i] == 1 and visit[i] == 0 :
            dfs(i)
    return

def bfs(x):
    q = collections.deque()
    q.append(x)

    while q:
        i = q.popleft()
        print(i+1, end= ' ')
        for j in range(n):
            if graph[i][j] == 1 and visit[j] == 0:
                visit[j] = 1
                q.append(j)
    return


n, m, v = map(int, sys.stdin.readline().split())
v -= 1

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    a, b = a-1, b-1
    graph[a][b] = 1
    graph[b][a] = 1

# dfs
visit = [0] * n
dfs(v)
print()

# bfs
visit = [0] * n
visit[v] = 1
bfs(v)
