import sys
input = sys.stdin.readline()

n = int(input.strip())
if n == 1:
    print(0)
    exit()
number = [n]

cnt = 0
while True:
    s = []
    for i in range(len(number)):
        if number[i] % 3 == 0:
            s.append(number[i] // 3)
        if number[i] % 2 == 0:
            s.append(number[i] // 2)
        s.append(number[i]-1)
    cnt += 1
    number = s
    if 1 in number:
        print(cnt)
        exit()




