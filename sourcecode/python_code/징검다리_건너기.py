def check(mid, stones, k):
    cnt = 0
    res = -2147000000
    for v in stones:
        if v < mid:
            cnt += 1
        else:
            if cnt > res:
                res = cnt
            cnt = 0
    if cnt != 0:
        res = cnt if cnt > res else res

    return res >= k

def solution(stones, k):
    s = 1
    e = max(stones)
    res = 0
    while s <= e:
        mid = (s + e) //2
        if check(mid, stones, k):
            e = mid - 1
        else:
            res = mid
            s = mid + 1

    return res

print(solution([1,0,0,7,8,9,3,2,1,0], 4)) #3
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) #3
print(solution([3,3,3,3],3)) #3
print(solution([4,9,2,5,3,8,7,1,4,3,5,8], 5)) #7