import sys
sys.setrecursionlimit(10 ** 5)

sys.stdin = open("input.txt", "rt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def move(x, y):
    if counts[x][y]: #counts가 이미 0이 아닌 경우에는
        return counts[x][y] # counts를 리턴!
    counts[x][y] = 1 # counts가 0인 경우에는 1로 (1일 살 수 있다.) 초기화
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            counts[x][y] = max(counts[x][y], move(nx,ny) + 1)
            # counts의 값은 현재 counts의 값과, 판다가 이동했을 때 얻을 수 있는 가장 큰 counts 값과 비교하여 더 큰 값을 갖는다.
    return counts[x][y]


n = int(sys.stdin.readline().strip())  # 대나무 숲의 크기
forest = list()  # 대나무 숲
counts = [[0] * n for _ in range(n)] # 이동 거리 계산용 배열
for _ in range(n):
    forest.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        counts[i][j] = move(i,j) # 해당 i,j 부터 움직였을 때 가장 오래 살아남을 수 있는 기간을 counts에 저장한다.

print(max(map(max, counts)))
