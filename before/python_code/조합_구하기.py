import sys
sys.stdin = open("input.txt","rt")

def dfs(L, s):
    global cnt
    if L == m: #depth가 m과 같으면
        for i in range(L):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s,n+1): #자기 자신 이후부터 뽑으므로 s부터 시작함.
                res[L] = i
                dfs(L+1, i+1)


if __name__ == "__main__":
    n,m=map(int,input().split())
    res = [0] * (n+1)
    cnt = 0
    dfs(0,1)
