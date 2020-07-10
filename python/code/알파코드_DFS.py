import sys
sys.stdin = open("input.txt","rt")

def dfs(L, position):
    global cnt, n
    if L >= n:
        cnt += 1
        for j in range(position):
            print(chr(res[j] + 64), end='')
        print()
    else:
        for i in range(1,27):
            if int(code[L]) == i and i < 10:
                res[position] = i
                dfs(L+1,position+1)
            elif i >= 10 and int(code[L]) == i//10 and int(code[L+1]) == i%10:
                res[position] = i
                dfs(L+2, position+1)

code = list(map(str,input()))
n = len(code)
res = [0] * n
code.insert(n, -1) #n번째에 -1 삽입
cnt = 0
dfs(0,0)
print(cnt)