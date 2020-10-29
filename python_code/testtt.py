def solution(N, number):
    if N == number:
        return 1

    s = [set() for x in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    print(s)

    for i in range(1, 8): #s = [{5}, {55}, {555} .. ]
        for j in range(i):
            for op1 in s[j]: #s[j] = {5} 와 같은 것
                for op2 in s[i - j - 1]: #i개에 따라 만들 수 있는 것이기 때문에, i-1개까지로 만들 수 있는 것들과 연산한다., 또한 역연산을 가능하게 하기 위해서 1-3 2-2 3-1과 같이!
                    s[i].add(op1 + op2) #s[i] 인 이유: i에 따라 만들 수 있는 값 ex) i = 2 면 5 2개로 만들 수 있는 값
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer

print(solution(5, 12))