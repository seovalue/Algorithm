def cut_two_letter(s):
    res = dict()
    for i in range(1, len(s)):
        if s[i - 1].isalpha() and s[i].isalpha():
            if s[i - 1] + s[i] in res.keys():
                res[s[i - 1] + s[i]] += 1
            else:
                res[s[i - 1] + s[i]] = 1
    return res


def get_intersection(s1, s2):
    total = 0
    for key, value in s1.items():
        if key in s2.keys():  # s2에 존재한다면
            total += min(s1[key], s2[key])
    return total


def get_union(s1, s2):
    total = sum(list(s1.values())) + sum(list(s2.values()))
    for key, value in s1.items():
        if key in s2.keys():
            total -= min(s1[key], s2[key])
    return total


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()  # 모두 소문자로 변경한다.

    set1, set2 = {}, {}
    # 두 글자씩 끊기
    set1 = cut_two_letter(str1)
    set2 = cut_two_letter(str2)
    if not set1 and not set2:
        return 65536

    i = get_intersection(set1, set2)
    u = get_union(set1, set2)

    if i == 0:
        return 0

    answer = int((i / u) * 65536)
    return answer