import sys
sys.stdin = open("input.txt","rt")

def dfs(L):
    global res
    if L == n:
        if res > max(money) - min(money):
            tmp = set()
            for j in range(3):
                tmp.add(money[j])
            if len(tmp) == 3:
                res = max(money) - min(money)
    else:
        for i in range(3):
            money[i] += coin[L]
            dfs(L+1)
            money[i] -= coin[L]

n = int(input())
coin = list()
money = [0] * 3
for i in range(n):
    coin.append(int(input()))
res = 2147000000
dfs(0)
print(res)


''' 순서대로 나눌 때
res = 2147000000

for i in range(1,n):
    for j in range(i+1,n):
        A = coin[:i]
        B = coin[i:j]
        C = coin[j:]
        maxVal = max(sum(A),sum(B),sum(C))
        minVal = min(sum(A),sum(B),sum(C))
        if res > (maxVal - minVal):
            res = (maxVal - minVal)

print(res)
'''

