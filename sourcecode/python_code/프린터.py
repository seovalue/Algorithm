def solution(priorities, location):
    answer = 0
    priorities = list(zip([i for i in range(len(priorities))], priorities))
    while priorities:
        p = priorities.pop(0)

        for pr in priorities:
            if pr[1] > p[1]:
                priorities.append(p)
                break
        else:
            answer += 1
            if p[0] == location:
                return answer
    return answer

print(solution([2,1,3,2], 2))