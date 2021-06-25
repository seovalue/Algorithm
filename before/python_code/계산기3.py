'''
알고리즘 스터디, 2021-01-17
'''
import sys
sys.stdin = open("input.txt","rt")

def calculate(a, b, operand):
    a, b = int(a), int(b)
    if operand == '+':
        return a + b
    if operand == '*':
        return a * b

for test_case in range(1, 11): # 테스트케이스는 총 10개
    length = int(input())
    operator = list()
    expression = input() # 수식 입력받기
    postfix = []

    # 후위표기식으로 만들기
    for e in expression:
        if e.isdigit():
            postfix.append(e)
        else: # 연산 기호인 경우
            if e == ")":
                while True:
                    if operator[len(operator) - 1] == "(":
                        operator.pop()
                        break
                    postfix.append(operator.pop())
                continue
            if e == "+":
                while operator and operator[-1] != "(":
                    postfix.append(operator.pop())
            if e == "*":
                while operator and operator[-1] == "*":
                    postfix.append(operator.pop())
            operator.append(e)
    while(len(operator) > 0):
        postfix.append(operator.pop())

    # 계산하기
    answer = 0
    index = 0
    while len(postfix) > 1:
        p = postfix[index]
        if not p.isdigit():
            answer = calculate(postfix[index-1], postfix[index-2], p)
            postfix.pop(index)
            postfix.pop(index-1)
            postfix.pop(index-2)
            postfix.insert(index - 2, answer)
            index -= 2
        index += 1
    print("#{} {}".format(test_case, answer))