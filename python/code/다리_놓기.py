import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 7)
T = int(sys.stdin.readline())
dp = {}


def combi(n,m):
    if (n,m) in dp.keys():
        return dp[(n,m)]
    if n == 0 or m == 0 or n == m:
        dp[(n,m)] = 1
        return 1
    res = combi(n-1,m-1) + combi(n-1,m)
    dp[(n,m)] = res
    return res

for _ in range(T):
    n,m = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(combi(m,n))+"\n")