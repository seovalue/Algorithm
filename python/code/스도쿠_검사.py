# import sys
# sys.stdin = open("input.txt","rt")

def Check(mat):
    for i in range(9):
        col_check = [0] * 10 #열 체크
        row_check = [0] * 10 #행 체크
        for j in range(9):
            col_check[mat[j][i]] = 1
            row_check[mat[i][j]] = 1

        if sum(col_check) != 9 or sum(row_check) != 9:
            return False

    for i in range(3):
        for j in range(3):
            area_check = [0]*10
            for k in range(3):
                for s in range(3):
                    area_check[mat[i*3+k][j*3+s]] = 1
            if(sum(area_check) != 9):
                return False
    return True

mat = [list(map(int,input().split())) for _ in range(9)]
if Check(mat):
    print("YES")
else:
    print("NO")