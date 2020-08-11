import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt","rt")

def dfs(node, target, value):
    if node == target:
        if result[target] == -1:
            result[target] = value
        if result[target] > value:
            result[target] = value
    else:
        for i in range(v):
            if graph[node][i] != 0 and visit[node] == 0:
                visit[node] = 1
                dfs(i,target,value + graph[node][i])
                visit[node] = 0



if __name__ == "__main__":
    v, e = map(int,input().split())
    k = int(input())
    k -= 1

    graph = [[0] * v for _ in range(v)]
    for i in range(e):
        start, end, weight = map(int,input().split())
        graph[start-1][end-1] = weight

    result = [-1] * v
    visit = [0] * v
    for i in range(v):
        if i != k:
            dfs(k,i,0)
        else:
            result[i] = 0

    for res in result:
        if res == -1:
            print("INF")
        else:
            print(res)

