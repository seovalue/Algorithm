import sys
sys.stdin = open("input.txt","rt")

def Coll(len):
    pick = horses[0]
    cnt = 1
    for horse in horses:
        if(abs(horse - pick) >= len):
            cnt += 1
            pick = horse
    return cnt

n, c = map(int, input().split())
horses = []
for i in range(n):
    horses.append(int(input()))
horses.sort()

left = horses[0]
right = horses[n-1]
diff = 0

while left <= right:
    mid = (left+right )// 2
    if Coll(mid) >= c:
        diff = mid
        left = mid + 1
    else:
        right = mid - 1

print(diff)