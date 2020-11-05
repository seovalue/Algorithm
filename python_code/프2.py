import itertools

def divide(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# 스타수열인지 확인
def is_star(s):
    n = len(s)
    answer = set()
    # x[n] != x[n+1] 인지 확인
    result = list(divide(s,2))
    for res in result:
        a, b = res[0], res[1]
        if a == b:
            return False

        if not answer:
            answer.add(a)
            answer.add(b)
        else:
            answer = answer.intersection({a,b})
            if not answer:
                return False

    return True


def solution(a):
    #애초에 하나밖에 없는 경우
    if len(a) <= 3:
        return 0
    if len(set(a)) == len(a):
        return 0

    size = len(a) - len(set(a))
    size = size * 2 if size % 2 == 0 else (size - 1) * 2
    # 부분 수열 구하기, 짝수개만 뽑도록
    # if len(a) % 2 == 0: #짝수이면
    #     size = len(a)
    # else:
    #     size = len(a) - 1
    for i in range(size, 3, -2):
        subseq = list(set(itertools.combinations(a,i)))
        for s in subseq:
            if len(set(s)) == len(s):
                continue
            if is_star(s):
                print(s)
                return len(s)

    return 0

print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))
print(solution([1,2,3,4]))
print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,22,24,25]))

