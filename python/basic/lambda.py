def plus_one(x):
    return x+1

print(plus_one(2))


#값을 넘기면 2를 더해서 리턴해줌
#변수명
plus_two = lambda x: x+2
print(plus_two(1))


#유용한 경우 : 내장함수의 인자로 사용될 때
a = [1,2,3]
print(list(map(plus_one, a)))
print(list(map(lambda x:x+1,a)))