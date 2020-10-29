def solution(word):
    answer = ''
    for w in word:
        if w.isupper(): #대문자인 경우
            answer += chr(155-ord(w))
        elif w.islower(): #소문자의 경우
            answer += chr(219-ord(w))
        else:
            answer += w
    return answer

print(solution("I love you"))

