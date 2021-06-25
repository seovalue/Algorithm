def initialize():
    dictionary = [chr(i) for i in range(65, 91)]
    dictionary.insert(0, 0)  # 인덱스를 1부터 하기 위해 맨 앞에 0을 삽입해줌.
    return dictionary


def solution(msg):
    answer = []
    dictionary = initialize()  # 사전을 초기화해줌.

    start = 0
    end = 1
    index = list()
    while True:
        if end > len(msg):
            break
        word = msg[start:end]
        if dictionary.count(word):  # 사전에 word가 존재하면
            if index:
                index.pop()
            index.append(dictionary.index(word))
            end += 1
        else:  # 존재하지 않으면
            start = end - 1
            dictionary.append(word)
            answer.append(index.pop())
            index = list()

    if index:  # 맨 마지막 값이 남아있는 경우
        answer.append(index.pop())
    return answer