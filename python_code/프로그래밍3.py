def separate(num):
    num = list(str(num))
    num = [int(x) for x in num]
    return num

def multiply(li):
    li.insert(0,1)
    for i in range(1, len(li)):
        li[0] *= li[i]
    return li[0]

def solution(pobi, crong):
    answer = 0

    p1, p2 = pobi
    c1, c2 = crong

    # 예외. 페이지 차이가 1이 나지 않으므로 올바른 페이지가 아니다.
    if abs(p1-p2) != 1 or abs(c1-c2) != 1:
        return -1

    # 페이지 수를 자릿수로 분리하기
    p1, p2 = separate(p1), separate(p2)
    c1, c2 = separate(c1), separate(c2)

    pobi_score = []
    crong_score = []
    # 자릿수 더하기
    pobi_score.append(max(sum(p1), sum(p2)))
    crong_score.append(max(sum(c1), sum(c2)))

    # 자릿수 곱하기
    pobi_score.append(max(multiply(p1), multiply(p2)))
    crong_score.append(max(multiply(c1), multiply(c2)))

    if max(pobi_score) > max(crong_score):
        return 1
    elif max(pobi_score) < max(crong_score):
        return 2
    else:
        return 0

# 포비가 이기면 1, 크롱이 이기면 2, 무승부는 0, 예외는 -1
print(solution([97,98],[197,198])) #0
print(solution([131,132],[211,212])) #1
print(solution([99,102],[211,212])) #-1
