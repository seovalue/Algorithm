ten_to_fifteen = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def notation(n,l): #n: 진법, l: 최대 길이
    answer = '0'
    number = 1
    while True:
        if len(answer) >= l:
            break
        result = []
        num = number
        while num:
            if (num % n) in ten_to_fifteen.keys():
                result.insert(0, ten_to_fifteen[num%n])
            else:
                result.insert(0, str(num % n)) #나머지를 저장하고
            num = num // n #num은 몫으로 업데이트
        answer += ''.join(result)
        number += 1
    return answer

def solution(n, t, m, p):
    answer = ''
    length = t * m #미리 구해놓아야하는 최대 길이
    string = notation(n, length)
    print(string)
    for i in range(0, len(string)):
        answer += string[(i*m+p)-1]
        if len(answer) == t:
            break
    return answer

print(solution(16,16,2,2))