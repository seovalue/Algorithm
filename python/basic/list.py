#리스트와 내장함수
a = [23, 12, 36, 53, 19]
print(a[:3])
print(len(a))

#옆으로 출력할 때에는 end=''를 붙임. 아니면 줄바꿈됨,
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

#인덱스번호까지 출력하고 싶을 때 (인덱스, 값)이 출력됨.
for x in enumerate(a):
    print(x)
#print(x[0]) 을 하면 인덱스만 출력됨.

#튜플은 값을 변경할 수 없다.

for index, value in enumerate(a):
    print(index, value)
print()

if all(60 > x for x in a):
    print("All satisfy")
else:
    print("Not satisfy")

#모두다 거짓일 때만 거짓
if any(15>x for x in a):
    print("YES")
else:
    print("NO")

