def solution(cryptogram):
    answer = ''
    for cry in cryptogram:
        if not answer:
            answer += cry
        else:
            word = answer[-1]
            if word == cry:
                answer = answer[:-1]
            else:
                answer += cry
    return answer

print(solution('browoanoommnaon')) #brown
print(solution('zyelleyz')) #""
print(solution("aabbccdeeffdghig")) #ghig