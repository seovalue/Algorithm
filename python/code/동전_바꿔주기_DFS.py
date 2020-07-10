import sys
sys.stdin = open("input.txt","rt")

def dfs(L,total):
    global cnt
    if L == k: #말단 노드
        if total == T:
            cnt += 1
    else:
        #가지가 뻗어나가야할 때에는 for문을 돌림.
        for i in range(cn[L]+1):
            dfs(L+1, total+(cv[L]*i))


T = int(input()) #지폐의 금액
k = int(input()) #동전의 가짓수
cv = list()
cn = list()

for i in range(k):
    a, b = map(int,input().split())
    cv.append(a)
    cn.append(b)
cnt = 0
dfs(0,0)

print(cnt)
