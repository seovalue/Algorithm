import sys, itertools
input = sys.stdin

def calc(numbers, operator):
    answer = numbers[0]
    for n, op in zip(numbers[1:], operator):
        if op == '+':
            answer += n
        elif op == '*':
            answer *= n
        elif op == '-':
            answer -= n
        elif op == '/':
            if answer < 0: #음수를 양수로 나눌 때
                answer = -1 * (abs(answer) // n)
            else:
                answer //= n
    return answer

n = int(input.readline().strip())
numbers = list(map(int, input.readline().split()))
num_of_op = list(map(int, input.readline().split()))
sample_op = ['+','-','*','/']
operator = [] #연산자
for i, j in zip(sample_op, num_of_op):
    if j >= 1: #연산자의 개수가 1이상이면, 개수만큼 operator에 넣는다!
        for _ in range(j):
            operator.append(i)

permutation_list = list(set((itertools.permutations(operator, len(operator)))))
answer = []
for p in permutation_list:
    answer.append(calc(numbers, p))

print(max(answer))
print(min(answer))
