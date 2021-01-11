import sys
sys.stdin = open("input.txt","rt")

def divide_and_conquer(x, y, n):
    # x: start_x, y: start_y, n: 자를 크기
    global count
    isSame = True # 모든 색이 같은지 확인하는 변수
    color = papers[x][y] #처음 색을 color에 저장하고, 비교함.

    for i in range(x, x+n):
        if not isSame:
            break
        for j in range(y, y+n):
            if color != papers[i][j]:
                isSame = False
                divide_and_conquer(x, y, n//2) # 2사분면
                divide_and_conquer(x, y + n//2, n//2) #3사분면
                divide_and_conquer(x + n//2, y, n//2) #1사분면
                divide_and_conquer(x+ n//2, y+ n//2, n//2) #4사분면
                break

    if isSame:
        count[color] += 1

N = int(sys.stdin.readline().strip())
papers = []
for _ in range(N):
    papers.append(list(map(int,sys.stdin.readline().split())))
count = {0:0, 1:0}
divide_and_conquer(0,0,N)
print(count[0])
print(count[1])