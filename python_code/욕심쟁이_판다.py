import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open("input.txt","rt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if check[x][y]: #체크가 0이 아닌 경우 (이미 다녀온 경우)
        return check[x][y] #체크를 리턴해줌.
    check[x][y] = 1 # 체크가 0인 경우에는 체크를 1로 초기화해줌.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위에 알맞은 nx,ny에 대하여 대나무개수도 더 많다면,
        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            # 해당 체크에 기존의 체크와, dfs를 돌고 난 뒤의 체크값에 +1 한 값 중 더 큰 값을 저장
            # 1을 더하는 이유는 기존 값에서 더 나아간 경우이므로 한칸을 추가해주는 것과 같다.
            check[x][y] = max(check[x][y], dfs(nx,ny) + 1)
    return check[x][y]


n = int(sys.stdin.readline())
forest = []
for _ in range(n):
    forest.append(list(map(int,sys.stdin.readline().split())))

check = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        check[i][j] = dfs(i,j) # 체크 배열에, dfs를 통해 얻은 해당 체크의 값을 저장.
print(max(map(max,check)))
