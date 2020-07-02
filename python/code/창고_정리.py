# import sys
# sys.stdin = open("input.txt","rt")

l = int(input())
move = list(map(int,input().split()))
m = int(input())

move.sort(reverse= True)

for i in range(m):
    move[0] -= 1
    move[l-1] += 1
    move.sort(reverse=True)

print(move[0] - move[l-1])


