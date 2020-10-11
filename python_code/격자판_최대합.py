# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
mat = []
for i in range(n):
    miniMat = list(map(int, input().split()))
    mat.append(miniMat)

Max = 0
diagTmp1 = 0
diagTmp2 = 0
for i in range(n):
    colTmp = 0
    rowTmp = 0
    diagTmp1 += mat[i][i]
    diagTmp2 += mat[i][n-i-1]
    for j in range(n):
        colTmp += mat[i][j]
        rowTmp += mat[j][i]
    Max = max(Max,rowTmp,colTmp)
Max = max(Max,diagTmp1,diagTmp2)

print(Max)
