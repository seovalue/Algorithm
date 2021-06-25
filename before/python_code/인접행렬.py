# import sys
# sys.stdin = open("input.txt","rt")

n,m= map(int,input().split())
mat = [[0] * (n) for _ in range(n)]

for i in range(m):
    tmp = list(map(int,input().split()))
    mat[tmp[0]-1][tmp[1]-1] = tmp[2]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j], end=' ')
    print()