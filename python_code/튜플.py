def separate(s):
    answer = []
    size = len(s)
    s = s[1:size - 1]  # 맨 처음과 맨 끝의 중괄호 제거

    flag = False
    tmp1 = []
    tmp2 = ''
    for i in range(len(s)):
        if s[i].isdigit():  # 숫자이면
            tmp2 += s[i]
        if s[i] == ',' and tmp2:
            tmp1.append(int(tmp2))
            tmp2 = ''
        if s[i] == '}':
            if tmp2:
                tmp1.append(int(tmp2))
            answer.append(tmp1)
            tmp1 = []
            tmp2 = ''
    answer = sorted(answer, key=lambda x: len(x))  # 원소 개수 순으로 정렬
    return answer


def solution(s):
    answer = []
    s = separate(s)  # 리스트로 분할
    for i in range(len(s)):
        if len(s[i]) == 1:
            answer.append(s[i][0])
        else:
            for j in range(len(s[i])):
                if s[i][j] not in answer:
                    answer.append(s[i][j])

    return answer


print(solution("{{123}}"))