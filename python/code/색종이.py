paper = [[0]  101 for _ in range(101)]
n = int(input())
area = 0
for i in range(n)
    x, y = map(int, input().split())
    for j in range(y, y+10)
        for k in range(x, x+10)
            paper[j][k] = 1


for row in paper
    if 1 in row
        area += sum(row)

print(area)