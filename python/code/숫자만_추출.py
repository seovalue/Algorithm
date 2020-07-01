# import sys
# sys.stdin = open("input.txt","rt")

string = input()

number = 0
for i in range(len(string)):
    if(string[i].isdigit()):
        number = number * 10 + int(string[i])
print(number)

cnt = 2
for i in range(2,number//2+1):
    if number % i == 0:
        cnt += 1
print(cnt)

