import sys
sys.stdin = open("input.txt","rt")

eq = input()
stack = []
res = ''
for x in eq:
    if x.isdecimal(): #x가 숫자인 경우
        res += x
    else: #숫자가 아닌 operand 인 경우
        if x == '(':
            stack.append('(')
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)







