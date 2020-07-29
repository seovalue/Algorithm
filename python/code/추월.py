import sys
sys.stdin = open("input.txt","rt")

n = int(input())
inCar = []
outCar = []
for _ in range(n):
    inCar.append(input())
for _ in range(n):
    outCar.append(input())

cnt = 0
incar = inCar.pop(0)
outcar = outCar.pop(0)
while inCar:
    if incar != outcar:
        cnt += 1
        idx = inCar.index(outcar)
        inCar.pop(idx)
        outcar = outCar.pop(0)
        continue

    incar = inCar.pop(0)
    outcar = outCar.pop(0)

print(cnt)


