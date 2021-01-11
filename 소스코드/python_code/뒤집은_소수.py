import sys
sys.stdin = open("input.txt","rt")
n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while(x > 0):
        t = x % 10 #나머지 값
        res = res * 10 + t #기존의 값을 10배해서 한자릿수 높이고, 새로 들어온 나머지 값을 뒤에 더해줌.
        x = x // 10 #몫
    return res
'''
소수인지 확인할 때, 약수인지 확인한다.
예를 들어, 16인 경우 16의 약수들은
1, 16
2, 8
4, 4
와 같이 곱셈으로 나타낼 수 있다.

이 때, 1과 자기자신은 제외하고 다음 차례가 2 부터이므로, 반복문은 절반까지 돌린다.
그리고 x와 절반까지 돌리는 그 값 i와의 나머지가 0이면 나누어 떨어진다. 즉, 약수인 것이므로 false를 리턴한다.
'''
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')