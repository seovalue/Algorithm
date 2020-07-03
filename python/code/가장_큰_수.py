import sys
sys.stdin = open("input.txt","rt")
num, m = map(int, input().split())
#숫자를 하나씩 분리
num = list(map(int,str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[: -m] #뒤쪽의 m개의 자료를 날려버림

res = ''.join(map(str,stack))
print(res)