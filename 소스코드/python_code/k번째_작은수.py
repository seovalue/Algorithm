import sys
sys.stdin = open("input.txt", "rt") #read text 모드

T = int(input())
for test_case in range(T):
    n,s,e,k = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers = numbers[s-1:e]
    numbers.sort()
    print('#%d %d' %(test_case+1, numbers[k-1]))


