# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

totalList = []

for i in range(n):
    totalList.append(list1[i])

for i in range(m):
    totalList.append(list2[i])

totalList.sort()

for item in totalList:
    print(item, end= ' ')