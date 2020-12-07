def calculate(s1, s2, op):
    if op == '+':
        return int(s1) + int(s2)
    elif op == '-':
        return int(s1) - int(s2)
    else:
        return int(s1) * int(s2)

def solution(s, op):
    answer = []
    for i in range(1,len(s)):
        answer.append(calculate(s[:i],s[i:], op))
    return answer

print(solution("1234","+"))
print(solution("987987","-"))
print(solution("31402","*"))
print(solution("11","+"))