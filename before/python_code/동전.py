import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

t = int(input())
n = int(input())
coin = list(map(int,input().split()))
m = int(input())
cnt = 0
while m > 0:
    c = coin.pop()
    cnt += (m // c)
    m = m % c

print(cnt)