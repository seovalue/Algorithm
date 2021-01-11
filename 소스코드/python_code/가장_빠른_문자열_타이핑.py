'''
알고리즘 스터디: 01.10 오후 10시, 온라인
3143. 가장 빠른 문자열 타이핑
예진
'''

T = int(input())
for test_case in range(1, T + 1):
    a, b = input().split()
    answer = len(a) + a.count(b) * (1 - len(b))
    print("#{} {}".format(test_case, answer))
