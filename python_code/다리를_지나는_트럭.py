def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    for truck in truck_weights:
        while True:
            if len(bridge) == bridge_length:
                bridge.pop(0)
                answer += 1
            if sum(bridge) + truck <= weight:
                bridge.append(truck)
                break
            else:
                bridge.append(0)

    return answer + bridge_length + len(bridge)

print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
print(solution(2,10,[7,4,5,6]))