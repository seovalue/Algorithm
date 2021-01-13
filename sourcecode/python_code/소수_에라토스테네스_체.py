import sys
sys.stdin = open("input.txt","rt")

n = int(input())
l = [0] * (n+1)

cnt = 0
for i in range(2,n+1):
    if(l[i] == 0):
        cnt += 1
        for j in range(i, n+1, i): #start, end, step (i씩 증가하도록 i의 배수로)
            l[j] = 1

print(cnt)

'''
에라토스테네스 체의 방법으로 푼다는 것이,
l = [0, 0, 0, 0, 0, ...] 으로 두고,
2부터 시작(prime 이므로)하여, 2의 l은 0이므로 0일때는 prime으로 체크하고,
2부터 n까지의 모든 2의 배수의 l을 1로 체크하여 걸러내는 것.
'''