def bfs(v, visit, adj):
    cnt = 0
    q = [(v, cnt)]
    while q:
        v, cnt = q.pop(0)
        if visit[v] == -1: #아직 방문하지 않았다면
            visit[v] = cnt #지나온 거리 값을 대입
            cnt += 1
            for e in adj[v]: #v에 인접한 에지들을 다시 큐에 삽입한다.
                q.append([e, cnt])


def solution(n, edge):
    answer = 0
    visit = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    for e in edge:
        x, y = e
        #서로 연결되어있음을 나타내준다.
        adj[x].append(y)
        adj[y].append(x)
    print(adj)
    bfs(1, visit, adj)
    for v in visit:
        if v == max(visit):
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))