import sys
sys.stdin = open("input.txt","rt")

'''
값이 특정 범위 안에 있을 때, 이분탐색을 사용한다.
'''
k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

#랜선의 길이를 오름차순 정렬
lines.sort()

#오름차순 정렬했으니 처음 값이 나올 수 있는 최대 길이
left = 0
right = lines[len(lines)-1]

while(left <= right):
    mid = (left+right)//2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt == n:
        print(mid)
        break
    elif cnt < n:
        right = mid - 1
    else:
        left = mid + 1







