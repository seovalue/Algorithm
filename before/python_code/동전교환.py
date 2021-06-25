import sys
sys.stdin = open("input.txt","rt")

def count(x, coin):
    count = 0
    for i in range(len(coin)):
        if(x <= 0): break
        count += x // coin[i]
        x %= coin[i]
    print(count)



n = int(input())
coin = list(map(int,input().split()))
coin.sort(reverse=True) #내림차순으로 정렬
m = int(input())

count(m,coin)