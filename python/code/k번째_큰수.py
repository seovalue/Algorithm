import sys
sys.stdin = open("input.txt", "rt") #read text 모드

n, k = map(int, input().split())
cards = list(map(int,input().split()))
result = set()

'''
i j m
1 2 3 4 5

뽑을 때, 1을 뽑았으면 뒤에서 j를 뽑고, j를 뽑고 난 이후부터 m을 뽑는다.
(중복되지 않게 뽑는다!)
'''


for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            result.add(cards[i]+cards[j]+cards[m])

result = list(result)
#result.sort()
#maxIdx = len(result)
#print(result[maxIdx - k])


result.sort(reverse=True)
print(result[k-1]) #k번째이므로!


