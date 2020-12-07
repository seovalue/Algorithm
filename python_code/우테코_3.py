# 남은 잔액으로 배팅을 할 수 있는지 확인
def check(money, bet):
    if money >= bet:
        return bet
    elif money < bet:
        return money

def solution(money, expected, actual):
    bet = 100 #초기 배팅 금액
    for expect, real in zip(expected, actual):
        if expect != real: #패한 경우
            money -= bet
            if money == 0:
                return money
            bet = check(money, bet*2)

        # 이겼으면 다음 판에도 100원을 건다.
        else: #이긴 경우
            money += bet
            bet = check(money, 100)
    return money

print(solution(1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H'],['T', 'T', 'H', 'H', 'T', 'T', 'H']))