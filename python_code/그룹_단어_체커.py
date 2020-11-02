import sys

input = sys.stdin

n = int(input.readline().strip())  # 단어의 개수
words = list(map(str, input.readline().strip()) for _ in range(n))
cnt = 0
for word in words:
    alpha = dict()
    flag = True
    for idx, w in enumerate(word):
        if w in alpha.keys():  # alpha에 존재하는 단어이면
            if abs(alpha[w] - idx) == 1:
                alpha[w] = idx
            else:
                flag = False
                break
        else:
            alpha[w] = idx
    if flag:  # 그룹 단어이면
        cnt += 1
print(cnt)
