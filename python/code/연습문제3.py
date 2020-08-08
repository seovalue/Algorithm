import sys
sys.stdin = open("input.txt","rt")

def dfs(start):
    if 0 in visit:
        answer.append(start + 1)
    if visit[start] == 0:
        visit[start] = 1
    for i in range(7):
        if graph[start][i] == 1 and visit[i] == 0:
            dfs(i)


n = 7
graph = [[0] * 7 for _ in range(7)]
visit = [0] * 7
answer = list()
for _ in range(8):
    i, j = map(int,input().split())
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

i = 0
while 0 in visit:
    if visit[i] == 0:
        dfs(i)
    i += 1

print(answer)