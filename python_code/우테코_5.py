def same(a, b):
    return True if a == b else False

def check(data, penter, pexit, pescape):
    i = 0
    while i < len(data):
        d = data[i]
        if same(d, penter) or same(d, pexit) or same(d, pescape):
            data.insert(i, pescape)
            i += 1
        i += 1
    return data

def solution(penter, pexit, pescape, data):
    n = len(penter) #길이
    data = [data[i:i+n] for i in range(0, len(data), n)] #데이터를 길이만큼 쪼갠다.
    # penter, pexit, pescape와 겹치면, 각 원소들 앞에 pescape을 붙이고, 문자열로 바꾸어준다.
    # 맨 앞과 맨 끝에 penter과 pexit을 더해준다.
    print(penter, pexit)
    data = penter +  ''.join(check(data, penter, pexit, pescape)) + pexit
    return data

a = solution("1100","0010","1001","1101100100101111001111000000")
answer = "110011011001100110010010111100111001110000000010"
if a == answer:
    print("hi")

