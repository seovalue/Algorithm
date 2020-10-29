# 약 6분 소요
def solution(money):
    answer = [0] * 9 #화폐의 종류만큼 0을 추가
    # 화폐를 coin에 저장함.
    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

    # 화폐가 큰 순으로 money와 나누었을 때 몫이 0보다 크다면 answer를 업데이트해줌. (해당 화폐로 출금할 수 있다.)
    i = 0
    while money > 0:
        if (money // coin[i]) > 0:
            answer[i] += (money // coin[i])
            money %= coin[i]
        i += 1

    return answer


print(solution(50237)) #[1,0,0,0,0,2,0,3,7]
print(solution(15000)) #[0,1,1,0,0,0,0,0,0]