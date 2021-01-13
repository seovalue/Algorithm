# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
fruit = []
for i in range(n):
    miniFruit = list(map(int,input().split()))
    fruit.append(miniFruit)

'''
0,2 
1,1 1,2, 1,3 
2,0 2,1 2,2 2,3 2,4
3,1 3,2 3,3
4,2
'''

total = 0
diamond = 1
flag = True
for i in range(n):
    if diamond == n:flag = False
    count = (n - diamond) // 2
    for j in range(count, count + diamond):
        total += fruit[i][j]
    if flag: diamond += 2
    else: diamond -= 2

print(total)


