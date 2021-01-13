def solution(number):
    result = 0
    number_list = [list(str(i)) for i in range(1, number+1)] #1부터 number까지의 리스트를 만든다.

    for num in number_list:
        if num.count('3') > 0:
            result += num.count('3')
        if num.count('6') > 0:
            result += num.count('6')
        if num.count('9') > 0:
            result += num.count('9')
    return result

print(solution(36))

