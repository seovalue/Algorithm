import sys
sys.stdin = open("input.txt",'rt')

n, m = map(int, input().split())

#확률은 모두 다 같다.
#가장 큰 합은 m+n이므로, m+n개의 0으로 이루어진 cnt 리스트를 만들어준다.
cnt = [0] * (m+n)
for i in range (1,n+1):
    for j in range(1,m+1):
        cnt[i+j-1] += 1

print()
maxVal = max(cnt)
maxProb = []



for index, value in enumerate(cnt):
    if(value == maxVal):
        maxProb.append(index+1)

maxProb.sort()
for prob in maxProb:
    print(prob, end=' ')




