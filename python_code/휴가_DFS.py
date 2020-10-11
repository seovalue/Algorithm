# import sys
# sys.stdin = open("input.txt","rt")

def dfs(L, total): #L은 날짜진행 (1,2), total은 금액 합
    global res
    if L > n:
        return
    if L == n:
        if res < total:
            res = total
    else:
        dfs(L+ct[L], total+cp[L]) #상담 하기
        dfs(L+1, total) #상담 안하기


n = int(input())
ct = list()
cp = list()
for i in range(n):
    a, b = map(int, input().split())
    ct.append(a)
    cp.append(b)
res = -2147000000
dfs(0,0)
print(res)
