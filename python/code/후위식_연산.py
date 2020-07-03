# import sys
# sys.stdin = open("input.txt","rt")
op = str(input())

res = 0
stack = []
for i in range(len(op)):
    res = 0
    if op[i].isdecimal():
        stack.append(int(op[i]))
    else:
        if op[i] == '+':
            res = sum(stack[-2:])
        elif op[i] == '-':
            res = stack[-2] - stack[-1]
        elif op[i] == '/':
            res = stack[-2] // stack[-1]
        elif op[i] == '*':
            res = stack[-2] * stack[-1]
        stack.pop()
        stack.pop()
        stack.append(res)


print(res)

