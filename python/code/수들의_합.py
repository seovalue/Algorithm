'''
연속적으로 더했을 때 k가 되는 경우
'''

import sys
sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())
A = list(map(int, input().split()))

#init
left = 0
right = 1
cnt = 0
total = A[0]

while True:
    if total < m: #합이 m보다 작은 경우에는 right를 옮겨줌
        if right < n:
            total += A[right]
            right += 1
        else:
            break
    elif total == m: #합이 m과 같은 경우에는 left를 옮김, 대신 total에서 left 값을 빼줌
        cnt += 1
        total -= A[left]
        left += 1
    else: #합이 m보다 큰 경우에도 left를 옮겨야함, 또한 total에서 left 값을 빼줌
        total -= A[left]
        left += 1

print(cnt)