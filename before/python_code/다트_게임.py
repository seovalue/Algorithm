def bonus(num, b):
    if b == 'S':
        return num
    elif b == 'D':
        return num ** 2
    else:
        return num ** 3


def solution(dartResult):
    answer = []
    dartResult = list(dartResult)  # 리스트로 변경

    index = -1

    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():  # 숫자인 경우
            if dartResult[i] == '1' and dartResult[i + 1] == '0':
                answer.append(10)
                i += 1
            else:
                answer.append(int(dartResult[i]))
            index += 1
        elif dartResult[i].isalpha():  # 문자인 경우
            answer[index] = bonus(answer[index], dartResult[i])  # 보너스를 계산한 점수로 업데이트
        else:  # 옵션인 경우
            if dartResult[i] == '*':  # 스타상인 경우
                size = len(answer)
                if size <= 1:
                    answer[0] = answer[0] * 2
                else:
                    answer[index] = answer[index] * 2
                    answer[index - 1] = answer[index - 1] * 2
            elif dartResult[i] == '#':  # 아차상인 경우
                answer[index] = answer[index] * (-1)
        i += 1

    return sum(answer)

dartResult = '10S2D*3T'
print(solution(dartResult))