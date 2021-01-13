import sys
sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())
songs = list(map(int, input().split()))

def Count(capacity):
    dvd = 1
    sum = 0
    for song in songs:
        if sum + song > capacity:
            dvd += 1
            sum = song
        else:
            sum += song
    return dvd


left = 0
right = sum(songs)
res = 0
while(left <= right):
    mid = (left + right) // 2
    if Count(mid) <= m:
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)


