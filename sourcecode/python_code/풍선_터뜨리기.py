import heapq

def solution(a):
    balloons = [(b,i) for i ,b in enumerate(a)] #풍선과 인덱스를 함께 저장
    result = len(a)
    left, right = balloons[:-1], balloons[1:]
    print(balloons)
    print(balloons[:-1])
    print(balloons[:1])
    heapq.heapify(left)
    heapq.heapify(right)
    print(left)
    print(right)

    NUM, IDX = 0, 1
    for i, balloon in enumerate(a[1:-1], 1):
        if balloon == right[0][NUM]:
            while right[0][IDX] <= i:
                heapq.heappop(right)
        if balloon > left[0][NUM] and balloon > right[0][NUM]:
            result -= 1
        heapq.heappush(left, (balloon, i))
    return  result

# 시간초과
# def solution(a):
#     answer = 2
#     for i in range(1,len(a)-1):
#         left = min(a[:i])
#         right = min(a[i+1:])
#
#         if left >= a[i] or right >= a[i]:
#             answer += 1
#
#     return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))


