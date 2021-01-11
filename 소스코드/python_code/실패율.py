def solution(N, stages):
    answer = {}
    user = len(stages)
    current = 0

    for n in range(1,N+1):
        if stages.count(n) != 0:
            answer[n] = stages.count(n)/(user-current)
        else:
            answer[n] = 0
        current += stages.count(n)


    answer = sorted(answer.items(), reverse= True, key = lambda x: (x[1], -x[0]))
    return [ans[0] for ans in answer]


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))