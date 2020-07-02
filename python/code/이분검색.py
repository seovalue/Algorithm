# import sys
# sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())
number = list(map(int,input().split()))

number.sort()

left = 0
right = len(number)-1

while(left <= right):
    mid = (left + right) // 2
    if(number[mid] == m):
        print(mid + 1)
        break
    elif(number[mid] < m):
        left = mid + 1
    elif(number[mid] > m):
        right = mid - 1
