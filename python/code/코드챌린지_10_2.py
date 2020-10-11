def cut(x,y,n,answer, arr):
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]: #하나라도 같은 수가 아니면
                cut(x,y,n//2, answer, arr)
                cut(x,y+n//2, n//2, answer, arr)
                cut(x+n//2, y, n//2, answer, arr)
                cut(x+n//2, y+n//2, n//2, answer, arr)
                return
    if check == 0: #모두 0일때
        answer[0] += 1
        return
    else:
        answer[1] += 1
        return

def solution(arr):
    answer = [0,0]
    n = len(arr)
    cut(0,0,n,answer,arr)
    return answer


print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))