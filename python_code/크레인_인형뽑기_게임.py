'''
해당 열의 가장 위에 있는 인형을 옮긴다.
해당 인형과 바구니의 top이 일치하면 포함하지 않는다.
해당 인형과 바구니의 top이 일치하지 않으면 바구니의 top에 삽입한다.
바구니에 남은 인형의 개수를 카운트한다.
'''


def solution(board, moves):
    answer = 0
    basket = list()  # 바구니

    while moves:
        move = moves.pop(0)  # 움직임을 순서대로 빼낸다.
        # move열 방향 순회
        doll = -1  # 인형 번호
        for i in range(len(board)):
            if board[i][move - 1] != 0:  # 0이 아닌 가장 위의 값
                doll = board[i][move - 1]
                board[i][move - 1] = 0
                break

        if doll == -1:
            continue
        if not basket:  # 바구니에 하나도 없으면
            basket.append(doll)
        else:  # 바구니에 인형이 있다면
            top = basket[0]  # 가장 위의 값
            if top == doll:  # 바구니의 가장 위의 인형과 삽입할 인형의 번호가 같을 때
                answer += 2
                basket.pop(0)  # 가장 위의 값 꺼냄
            else:
                basket.insert(0, doll)  # 가장 위에 doll을 삽입한다.
    return answer