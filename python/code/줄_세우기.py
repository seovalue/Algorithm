import sys
sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
students = [i for i in range(1,n+1)]

for idx, number in enumerate(numbers):
    if number == 0:
        continue
    else:
        afterIdx = idx - number
        students.pop(idx)
        students.insert(afterIdx, idx+1)

for student in students:
    print(student, end= ' ')
