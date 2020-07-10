import sys
sys.stdin = open("input.txt","rt")

def dfs(L, total, time):
    global res
    if time > m:
        return
        # dfs의 중간에 return을 해주면, 아래 코드에서 문제를 풀었을 때 경우에
        # 어긋나는 것이므로 빠져나와 문제를 풀지 않았을 때로 넘어가게 된다.
    if L == n:
        if total > res:
            res = total
    else:
        dfs(L+1, total+pv[L],time+pt[L]) #문제를 풀었을 때
        dfs(L+1, total, time) #안풀었을 때



if __name__ == "__main__":
    n,m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int,input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000 #가장 작은 수
    dfs(0,0,0) #Level(1번, 2번 등), 총점, 시간
    print(res)


