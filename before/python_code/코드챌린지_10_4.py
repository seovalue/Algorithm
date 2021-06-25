import itertools
def get_substring(string):
    substring = []
    for i in range(len(string)):
        for j in range(len(string) - i):
            substring.append(string[j:j+i+1])

    return substring

def compare_string(string):
    size = len(string)
    for i in range(size):
        comp = string[i]
        for j in range(size):
            if comp != string[j]:
                return False
    return True


def solution(s):
    answer = 0
    if compare_string(s):
        return answer

    strings = get_substring(s)
    print(strings)

    for string in strings:

        size = len(string)
        if size == 1:
            continue
        if compare_string(string): #모두 같으면
            continue
        idx = [i for i in range(0, size)]
        combs = list(itertools.combinations(idx, 2))

        max_val = 0
        for comb in combs:
            x, y = comb
            if string[x] != string[y]:
                max_val = abs(x-y) if abs(x-y) > max_val else max_val

        answer += max_val

    return answer

print(solution("baby"))
# import itertools
#
# pool = list('baby')
# for i in range(1,len(pool)+1):
#     print(list(map(''.join, itertools.combinations(pool,i)))) # 3개의 원소로 수열 만들기