import sys
sys.stdin = open("input.txt","rt")

def dfs(idx, sum):
    if sum > total // 2:
        return
    if idx == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else: #두갈래로 나눔.
        dfs(idx+1, sum+num[idx])
        dfs(idx+1, sum)

if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    total = sum(num)
    dfs(0,0)
    print("NO")

