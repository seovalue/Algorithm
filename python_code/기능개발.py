def work_per_day(progress, speed):
    answer = (100-progress) // speed
    if progress % speed != 0:  # 나누어떨어지지 않으면
        answer += 1
    return answer


def solution(progresses, speeds):
    answer = []
    times = []
    # 몇 일간 작업 후 배포가 가능한지를 times 배열에 저장
    for i in range(len(progresses)):
        times.append(work_per_day(progresses[i], speeds[i]))

    idx = 0 #배포되는 작업의 인덱스
    count = 1
    while True:
        if sum(answer) == len(times):
            break
        release = times[idx] #배포될 작업에 소요된 시간
        if idx == len(times)-1: answer.append(count)
        for i in range(idx+1, len(times)):
            if times[i] <= release:
                count += 1
            else:
                answer.append(count)
                count = 1
                idx = i
                break
        if count != 1: #answer에 저장되지 않고 남은 값
            answer.append(count)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))