import sys
sys.stdin = open("input.txt","rt")

n = int(input())
sports = []
for i in range(n):
    h, w = map(int, input().split())
    sports.append((h,w))
sports.sort(reverse=True)
#키의 역순으로 정렬함.

largest = 0
cnt = 0

for h,w in sports:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)

