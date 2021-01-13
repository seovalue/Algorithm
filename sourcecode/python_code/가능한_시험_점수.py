'''
알고리즘 스터디: 01.10 오후 10시, 온라인
3752번, 가능한 시험 점수
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # print('#{}'.format(test_case), end=' ')
    t = int(input())  # test case의 수를 입력받는다.
    scores = list(map(int, input().split()))  # 가능한 점수의 목록을 입력받는다.
    # 가능한 점수를 결과에 추가했는지 확인하는 배열
    # 가능한 최대 점수까지의 배열을 생성한다.
    checker = [1] + [0] * sum(scores)
    result_score = [0]

    '''
    이미 푼 점수에 새로운 해당 점수의 문제를 풀었을 경우에 얻을 수 있는 점수를 추가한다.
    '''
    for score in scores:
        temp = list(result_score)
        for n in temp:
            if not checker[score + n]:
                checker[score + n] = 1
                result_score.append(score + n)

    print("#{} {}".format(test_case, len(result_score)))