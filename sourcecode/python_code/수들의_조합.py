#import sys
#sys.stdin = open("input.txt","rt")

def dfs(L, s, total):
    global cnt, number
    if L == k: #depth가 m과 같으면
        if total % m == 0:
            cnt += 1
    else:
        for i in range(s,len(number)): #자기 자신 이후부터 뽑으므로 s부터 시작함.
                res[L] = number[i]
                dfs(L+1, i+1, total+number[i])


if __name__ == "__main__":
    n,k=map(int,input().split())
    number = list(map(int,input().split()))
    m = int(input())

    res = [0] * (n+1)
    cnt = 0
    total = 0
    dfs(0,0,total)
    print(cnt)
