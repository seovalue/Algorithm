import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m,k = map(int,input().split())
matrix = [[0] * m for _ in range(n)]

idx_i = ((k-1) // m)+1
idx_j = ((k-1) % m) +1

dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = 1

if k == 0:
    idx_i = n
    idx_j = m

#k번째 칸까지 시행
for i in range(1, idx_i+1):
    for j in range(1, idx_j+1):
        if i == 1 and j == 1: continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
result = dp[idx_i][idx_j]

if k == 0:
    print(result)
    exit(0)

dp = [[0] * (m+1) for _ in range(n+1)]
dp[idx_i][idx_j] = 1
#k부터 마지막 칸까지 시행
for i in range(idx_i, n+1):
    for j in range(idx_j, m+1):
        if i == idx_i and j == idx_j: continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

result *= dp[n][m]

print(result)


