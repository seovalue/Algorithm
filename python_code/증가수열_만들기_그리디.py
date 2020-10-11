import sys
sys.stdin = open("input.txt","rt")

n = int(input())
li = list(map(int,input().split()))

left = 0
right = n-1
last = 0

empty = []
output = ''
while(left <= right):

    #last(지난 값)보다 큰 값들만 empty에 집어 넣음. (증가수열이기 때문)
    if(li[left] > last):
        empty.append((li[left], 'L'))
    if li[right]>last:
        empty.append(((li[right],'R')))
    empty.sort()
    if(len(empty) == 0):
        break
    else:
        #더 작은 값을 선택함.
        output += empty[0][1]
        last = empty[0][0]
        if empty[0][1] == 'L':
            left += 1
        else:
            right -= 1
    empty.clear()
print(output)