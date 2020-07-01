# import sys
# sys.stdin = open("input.txt","rt")

T = int(input())
for test_case in range(T):
    string = input()
    string = string.lower()
    length = len(string)
    Pass = True
    for i in range(length // 2):
        if(string[i] != string[length-i-1]):
            Pass = False
    if Pass:
        print("#%d YES" %(test_case+1))
    else:
        print("#%d NO" %(test_case+1))



