import sys

sys.stdin = open("input.txt","rt")
vowel = ['a','e','i','o','u']

while True:
    string = input()
    if string == 'end':
        break

    flag = False
    cnt_vowel = 0
    cnt_conso = 0

    for i in range(len(string)):
        if i+1 < len(string) and string[i] == string[i+1]:
            if not (string[i] == 'e' or string[i] == 'o'):
                flag = False
                break
        if cnt_vowel >= 3 or cnt_conso >= 3:
            flag = False
            break
        if string[i] in vowel:
            flag = True
            cnt_vowel += 1
            cnt_conso = 0
            if cnt_vowel >= 3: flag = False
        else:
            cnt_vowel = 0
            cnt_conso += 1
            if cnt_conso >= 3: flag = False


    if flag == False:
        print("<%s> is not acceptable." %(string))
    else:
        print("<%s> is acceptable." %(string))










