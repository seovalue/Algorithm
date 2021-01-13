# import sys
# sys.stdin = open("input.txt","rt")

def dfs(value):
    global n, cnt
    global mat
    if value == n:
        cnt += 1
    else:
        for i in range(len(mat[0])):
            if mat[value][i] == 1 and visit[value] == 0:
                visit[value] = 1
                dfs(i)
                visit[value] = 0



if __name__ == "__main__":
    n,m = map(int,input().split())
    mat = [[0] * n for _ in range(n)] #행렬 초기화
    visit = [0] * n
    for i in range(m):
        s, e = map(int, input().split())
        mat[s-1][e-1] = 1
    n -= 1 #인덱스가 0부터 시작하는 것과 맞춰주기 위해
    cnt = 0
    dfs(0)
    print(cnt)





