import sys
sys.stdin = open("input.txt","rt")

n = int(input())
box = list(map(int,input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1,n):
    maxVal = 0
    for j in range(0,i):
        if box[j] < box[i]:
            maxVal = dp[j] if dp[j] > maxVal else maxVal
    dp[i] = maxVal+1
print(max(dp))
