'''
21-02-10 알고리즘 스터디, sum
'''
import sys
sys.stdin = open("input.txt","rt")

for _ in range(10):
    case = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0
    for x in range(100):
        row_sum = col_sum = 0
        for y in range(100):
            row_sum += array[x][y]
            col_sum += array[y][x]
        max_value = max(row_sum, col_sum, max_value)

    diag_right_sum = diag_left_sum = 0
    for z in range(100):
        diag_right_sum += array[z][z]
        diag_left_sum += array[z][99 - z]
    max_value = max(max_value, diag_right_sum, diag_left_sum)

    print("#{} {}".format(case, max_value))
