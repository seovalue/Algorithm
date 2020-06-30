#문자열과 내장함수
msg = 'It is Time'

#대문자로 통일
print(msg.upper())
#원본은 그대로 유지
print(msg)
#소문자화
print(msg.lower())

tmp = msg.upper()
#T의 인덱스 번호를 출력함
print(tmp.find('T'))
#T의 개수를 출력함
print(tmp.count('T'))
#문자열 슬라이스 0~1까지의 인덱스를 출력함.
print(msg[:2])
print(msg[3:6])

#문자열의 길이
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end='')
print()
for x in msg:
    print(x, end='')
print()
for x in msg:
    if x.isupper():
        print(x, end='')
    if x.islower():
        print(x, end=' ')

print()
#공백 제거!
for x in msg:
    if x.isalpha():
        print(x,end='')

print()
#아스키 ord -> ASCII 넘버를 출력해줌, A = 65, Z = 90
tmp = 'AZ'
for x in tmp:
    print(ord(x))

print()
tmp = 'az'
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp)) #아스키 넘버의 문자로 출력함.

