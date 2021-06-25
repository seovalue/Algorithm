import sys
# sys.stdin = open("input.txt", "rt") #read text 모드
'''
첫째 줄에 n과 k가 빈칸을 두고 주어진다.
첫째 줄에 n의 약수들 중 k번째로 작은 수를 출력한다. n의 약수의 개수가 k개보다 적어서 k번째 약수가 존재하지 않을 경우에는 -1 출력.
'''
n, k = map(int, input().split())
cnt = 0
#n까지 for문을 돌림
for i in range(1, n+1):
    #약수인 경우
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: #정상적으로 끝났다면
    print(-1)
