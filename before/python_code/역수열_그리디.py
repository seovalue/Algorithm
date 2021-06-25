# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
revSeq = list(map(int, input().split()))
seq = [0] * n

number = 1
for num in revSeq:
    cnt = 0
    for i in range(len(seq)):
        if cnt == num:
            while seq[i] != 0:
                i += 1
            seq[i] = number
            number += 1
            break
        if seq[i] < number:
            if seq[i] == 0:
                cnt += 1

for i in seq:
    print(i, end=' ')