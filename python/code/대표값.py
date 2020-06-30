import sys
sys.stdin = open("input.txt", "rt") #read text 모드

n = int(input())
math = list(map(int, input().split()))

#round 함수는 두번째 인자가 생략되면 소수 첫째자리에서 반올림한다.
avg = round(sum(math)/n)
min = 0
idx = 0
diff = 100

for index, grade in enumerate(math):
    if(abs(grade-avg) == diff):
        if(grade > min):
            idx = index
            min = grade
    elif(abs(grade - avg) < diff):
        idx = index
        min = grade
        diff = abs(grade-avg)

print(avg,idx+1)

