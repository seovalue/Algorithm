import sys
sys.stdin = open("input.txt","rt")
stack = []
T = int(input())

for test_case in range(1, T + 1):
    line = list(map(str,input()))
    count = 0
    for i in range(len(line)):
        if line[i] == '(':
            stack.append('(')
        elif line[i] == ')' and i != 0:
            if line[i-1] == '(':
                stack.pop()
                count += len(stack)
            else:
                stack.pop()
                count += 1
    print("#{} {}".format(test_case, count))

