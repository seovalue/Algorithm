import sys, heapq
sys.setrecursionlimit(10**5)
inf = float('inf')

def dijkstra(v,k,graph):
    dist = [inf for _ in range(v+1)]
    dist[k] = 0

    hq = []
    heapq.heappush(hq, [0,k]) #heapq에 [cost,node]를 넣음

    while hq:
        temp = heapq.heappop(hq) #cost가 최소인 노드
        cost = temp[0]
        node = temp[1]

        if cost > dist[node]:
            continue

        for i in graph[node]:
            neighbor = i[0]
            cost_i = dist[node] + i[1]

            if cost_i < dist[neighbor]:
                dist[neighbor] = cost_i
                heapq.heappush(hq, [cost_i, neighbor])
    return dist

v, e = [int(x) for x in sys.stdin.readline().split()]
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    start, end, weight = [int(x) for x in sys.stdin.readline().split()]
    graph[start].append([end,weight])

answer = dijkstra(v,k,graph)

for dis in answer[1:]:
    print(dis if dis != inf else 'INF')