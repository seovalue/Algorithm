def rotate(key):
    return list(zip(*key[::-1]))

def check(start_x, start_y, key, lock, wide_size, start, end):
    wide_list = [[0] * wide_size for _ in range(wide_size)]
    # wide_list에 key 추가, 시작점에서 위아래만큼 key룰 추가하는 것임.
    for i in range(len(key)):
        for j in range(len(key)):
            wide_list[start_x+i][start_y+j] += key[i][j]

    # wide_list에 lock을 추가하며 기존 값과 더한다.
    for i in range(start, end):
        for j in range(start, end):
            wide_list[i][j] += lock[i - start][j- start]
            if wide_list[i][j] != 1:
                return False

    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    start = m - 1  #start point of lock in wide_list
    end = start + n # end point of lock in wide_list
    wide_size = n + start * 2 #size of wide_list

    # To move a key over a fixed lock position
    for i in range(0, 4): # origin, 90, 180, 270
        for j in range(end):
            for k in range(end):
                if check(j, k, key, lock, wide_size, start, end):
                    return True
        key = rotate(key)
    return False



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[1, 0, 0], [0, 1, 1], [1,0, 1]],[[0, 1, 1, 1], [1, 1, 1,1], [1, 1, 1,1],[1,1,1,1]]))
print(solution([[1,1],[1,1]], [[0,0,0],[1,1,1],[1,1,1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 1, 0], [1, 1, 0], [1, 0, 1]],
                    [[1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 1, 0, 1, 1],
                     [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))

# print(list(zip(*a[::-1])))

# a = [[1,2,3],[4,5,6],[7,8,9]]
#
# i = len(a)
# while i >= 0:
#     for j in range(i):
#         l = 1
#         for k in range(j, j-l, -1):
#             print(a[j][k])
#             l -= 1
#             if l

