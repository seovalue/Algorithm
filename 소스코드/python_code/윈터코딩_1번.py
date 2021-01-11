def solution(n, delivery):
    answer = [-1 for i in range(0, n+1)] #재고를 나타내는 배열, 재고가 있으면 1, 없으면 0, 모르면 -1
    delivery = sorted(delivery, key=lambda x: -x[2])
    for d in delivery:
        g1, g2, delivered = d #g1: 굿즈1, g2: 굿즈2, delivered : 배송 여부
        if delivered == 1: #배송된 경우
            answer[g1] = answer[g2] = 1 #두 상품 모두 재고가 있다고 표시한다.
        elif delivered == 0:
            # 하나는 재고가 있고, 하나는 아직 모르는 경우
            if answer[g1] == 1 and answer[g2] == -1:
                answer[g2] = 0
            if answer[g2] == 1 and answer[g1] == -1:
                answer[g1] = 0

            # 하나가 없고, 하나는 아직 모르는 경우 -> 그대로 유지
            # 둘다 모르는 경우 -> 그대로 유지

    answer = [str(i) for i in answer[1:]]
    answer = ''.join(answer).replace('-1','?').replace('0','X').replace('1','O')

    return answer

print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]])) #"O?O?X?"
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]])) #"O?O?XXO"
