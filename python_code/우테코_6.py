def cheating(scores):
    result = set()
    code = list(scores.keys())
    score = list(scores.values())
    score = [list(filter(lambda x : x != -1, s)) for s in score] #푼 문제들만 필터링

    for i in range(1,len(score)):
        if len(score[i-1]) < 5 or len(score[i]) < 5:
            continue
        if score[i-1] == score[i]:
            result.add(code[i-1])
            result.add(code[i])
    return list(result)

def solution(logs):
    scores = dict()
    for log in logs:
        code, number, score = log.split(' ')
        if code not in scores.keys():
            scores[code] = [-1] * 101 #점수표 만들기
        scores[code][int(number)] = [number, score]

    answer = cheating(scores)
    if answer:
        return sorted(answer)
    else:
        return ['None']

print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]))
print(solution(["1901 10 50", "1909 10 50"]))
print(solution(["0001 1 10", "0001 2 10",  "0001 3 10", "0002 1 10", "0002 3 10", "0002 4 10"]))