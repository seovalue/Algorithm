import sys
sys.stdin = open("input.txt","rt")

result = ''
tmp = input()
visit = [0] * len(tmp)
string = list(tmp)

temp = sorted(list(tmp))

idx = string.index(temp[0])
keep_idx = idx
visit[idx] = 1
temp.pop(0)
print(string[idx])
temp = string[idx+1:]
find_idx = string[idx+1:]
flag = 0
for _ in range(len(string)):
    if len(temp) == 0:
        temp = string[:keep_idx]
        find_idx = string[:keep_idx]
        flag = 1
    temp = sorted(temp)
    idx = find_idx.index(temp[0])
    if flag == 0:
        visit[idx+keep_idx+1] = 1
    else:
        visit[idx] = 1
    temp.pop(0)

    result = ''
    for i in range(len(visit)):
        if visit[i] == 1:
            result += string[i]
    print(result)





