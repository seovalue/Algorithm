import sys
sys.stdin = open("input.txt","rt")

def dfs(L,total):
    global res
    if L == k:
        if 0 < total <= s:
            res.add(total)

    else:
        dfs(L+1, total+chu[L])
        dfs(L+1, total-chu[L])
        dfs(L+1, total)



k = int(input())
chu = list(map(int,input().split()))
s = sum(chu)
res = set()
dfs(0,0)
print(s-len(res))


