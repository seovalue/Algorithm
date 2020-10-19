def checkCorrect(p):
    stack = []
    p = list(p)
    while p:
        p1 = p.pop(0)
        if not stack:
            stack.append(p1)
            continue
        if p1 == ')' and stack[0] == '(':
            stack.pop(0)
            continue
        stack.append(p1)

    if not stack:  # 스택이 비어있으면
        return True
    else:
        return False


def makeBalance(p):
    p = list(p)
    u, v = '', ''
    cnt1, cnt2 = 0, 0
    while p:
        p1 = p.pop(0)
        u += p1
        if p1 == '(':
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == cnt2:
            break
    v = ''.join(p)
    return u, v


def reverse(p):
    answer = ''
    for i in range(len(p)):
        if p[i] == '(':
            answer += ')'
        else:
            answer += '('
    return answer


def step(p):
    if not p:
        return p
    u, v = makeBalance(p)
    if checkCorrect(u):
        return u + step(v)
    else:
        return '(' + step(v) + ')' + reverse(u[1:len(u) - 1])


def solution(p):
    if checkCorrect(p):
        return p
    answer = step(p)

    return answer