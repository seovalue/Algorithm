def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        tmp = bin(num1 | num2)[2:] #or을 쓴 이유는 하나라도 1이면 1이기 때문.
        if len(tmp) < n: #n보다 길이가 작을 때
            tmp = '0'*(n-len(tmp)) + tmp #n의 길이를 갖도록 앞에 0을 붙인다.
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
    return answer