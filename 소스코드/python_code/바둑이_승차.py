import sys
sys.stdin = open("input.txt","rt")

'''
C를 넘지 않으면서, 바둑이를 가장 무겁게 태우는 방법
모든 경우의 수를 다 탐색하고, 무게가 가장 C보다 작으면서 가까운 값을 출력한다.
'''
def dfs(idx, total):
    global result
    if total > c:
        return
    if idx == n:
        if total > result:
            result = total
    else:
        dfs(idx+1, total+dogs[idx])
        dfs(idx+1, total)

if __name__ == "__main__":
    c, n = map(int, input().split())
    result = -2147000000
    dogs = [0]*n
    for i in range(n):
        dogs[i] = int(input())
    dfs(0,0)
    print(result)

