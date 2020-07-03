import sys
sys.stdin = open("input.txt","rt")

def dfs(L):
    global cnt
    if L == m:
        for j in range(m):
            print(marble[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1): #marble[L] 자리에 i 값 넣고
            marble[L] = i
            dfs(L+1) #n번 반복


if __name__ == "__main__":
    n, m = map(int, input().split())
    marble = [0] * n
    cnt = 0
    dfs(0)
    print(cnt)

#중복을 허락하여 m번을 뽑는다.
