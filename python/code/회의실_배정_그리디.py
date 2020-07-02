import sys
sys.stdin = open("input.txt","rt")

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
#x가 meeting의 원소인데, 정렬 순위가 end, start 순으로 하여라.
meeting.sort(key=lambda x : (x[1], x[0]))

end = 0
cnt = 0
for s, e in meeting:
    if s >= end:
        end = e
        cnt += 1
print(cnt)