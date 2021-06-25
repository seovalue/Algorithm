import itertools

def isUnique(comb, relation):
    check = set()
    for i in range(len(relation)):
        temp = list()
        for j in range(len(comb)):
            temp.append(relation[i][int(comb[j])])
        check.add(tuple(temp))
    if len(check) == len(relation):
        return True
    return False

def checkSubstr(str, strset):
    for s in strset:
        if len(s) < len(str): #확인하려는 문자열의 길이가 더 길면
            cnt = 0
            for i in range(len(s)):
                if s[i] in str:
                    cnt += 1
            if cnt == len(s):
                return False
    return True

def solution(relation):
    answer = []
    # 행과 열의 크기
    row = len(relation)
    col = len(relation[0])

    attribute = [str(i) for i in range(col)] # 구분 가능한 속성

    size = 1
    while size <= col:
        combs = list(itertools.combinations(attribute, size))
        for comb in combs:
            if isUnique(comb, relation):
                combStr = ''.join(comb)
                if checkSubstr(combStr, answer): #기존의 answer 집합안에 속해있는 것이 아니라면
                    answer.append(combStr)
        size += 1
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

