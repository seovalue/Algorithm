from collections import deque
import sys
sys.stdin = open("input.txt","rt")

n = int(input())
emo = [[-1] * 1001 for _ in range(1001)]
emo[1][0] = 0
q = deque()
q.append((1,0))

while q:
    screen, clipboard = q.popleft()

    if emo[screen][screen] == -1:
        emo[screen][screen] = emo[screen][clipboard] + 1
        q.append((screen,screen))
    if screen + clipboard <= n and emo[screen][clipboard] == -1:
        emo[screen + clipboard][clipboard] = emo[screen][clipboard]+1
    if screen-1 >= 0 and emo[screen - 1][clipboard] == -1:
        emo[screen-1][clipboard] = emo[screen][clipboard]+1
        q.append((screen-1, clipboard))


ans = -1
for i in range(n):
    if emo[n][i] != -1:
        print(emo[n][i])
        if ans == -1 or ans > emo[n][i]:
            ans = emo[n][i]

