import itertools, sys
sys.setrecursionlimit(10 ** 5)

# a = [0,1,2,3]
# print(list(itertools.combinations(a,3

def solution(n, edges):
    answer = []
    dist = [[0]* (n+1) for _ in range(n+1)]
    for edge in edges:
        a, b = edge
        dist[a][b] = 1
        dist[b][a] = 1

    temp = [i for i in range(1, n+1)]
    combs = list(itertools.combinations(temp,3))

    for comb in combs:
        cases = list(itertools.combinations(comb,2))
        distances = list()
        for case in cases:
            start, end = case

            visit = [0 for _ in range(n+1)]
            def dfs(start, end, count):
                if start == end:
                    return count
                visit[start] = 1
                for i in range(1, n):
                    if dist[start][i] == 1 and visit[i] == 0:
                        dfs(i, end, count+1)


            distances.append(dfs(start, end, 0))
        distances = sorted(distances)
        answer.append(distances[(len(distances)-1)// 2])
    return max(answer)


print(solution(5, [[1,5],[2,5],[3,5],[4,5]]))
