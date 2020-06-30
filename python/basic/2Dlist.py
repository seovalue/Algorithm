# 2차원 리스트의 생성

a = [0] * 10 #0으로 초기화된 len = 10의 1차원 리스트가 생김.
print(a)


b = [[0]*3 for _ in range(3)] #일차원 리스트를 세번 만듦.
print(b)
b[0][0] = -1
print(b)

#x가 [0,0,0] 하나를 가리킴.
for x in b:
    print(x)

for x in b:
    for y in x:
        print(y, end=' ')
    print()