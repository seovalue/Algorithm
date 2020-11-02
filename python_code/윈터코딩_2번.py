def rotate(text, rotation):
    answer = ''
    if abs(rotation) == len(text):
        if rotation > 0:
            return text
        else:
            return text[::-1]
    text = list(text)
    flag = True if rotation > 0 else False
    for _ in range(abs(rotation)):
        if flag: #양수로 회전한 결과인 경우
            tmp = text.pop(0)
            text.append(tmp)
        else:
            tmp = text.pop(-1)
            text.insert(0,tmp)
    return ''.join(text)



def solution(encrypted_text, key, rotation):
    answer = ''
    # 회전하기 이전의 암호화 문장으로 돌려준다.
    encrypted_text = rotate(encrypted_text, rotation)
    for k, e in zip(key, encrypted_text):
        step = ord(k) - 96
        if ord(e) - step < 97: #소문자 a보다 벗어나면
            plain = chr(ord('z') - (96 - (ord(e) - step)))
        else:
            plain = chr(ord(e) - step)
        answer += plain
    return answer

print(solution("qyyigoptvfb","abcdefghijk", 3))
print(solution("vtunz", "hello", -3))
