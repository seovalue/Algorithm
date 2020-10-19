import itertools


def separate(exp):
    operator = set()
    expression = []
    num = ''
    for e in exp:
        if not e.isdigit():
            operator.add(e)
            expression.append(int(num))
            expression.append(e)
            num = ''
        else:
            num += e
    if num:
        expression.append(int(num))
    return operator, expression

def calculate(expression, operator):
    for i in range(len(operator)):
        op = operator[i]
        while expression.count(op): #해당 오퍼레이터가 존재하면
            idx = expression.index(op)
            res = 0
            if op == '*':
                res += expression[idx-1] * expression[idx+1]
            elif op == '+':
                res += expression[idx - 1] + expression[idx + 1]
            else:
                res += expression[idx - 1] - expression[idx + 1]
            for _ in range(3):
                expression.pop(idx-1)

            if not expression:
                return abs(res)
            expression.insert(idx-1, res)

def solution(expression):
    op, expression = separate(expression) # 연산자와 expression을 리스트로 변경
    op_case = list(itertools.permutations(op,len(op)))

    maxResult = []
    for op in op_case:
        exp = expression[:] #shallow copy
        maxResult.append(calculate(exp, op))
    return max(maxResult)

print(solution("50*6-3*2"))