import time
start = time.time()
d, n = 1, 1
def get_binomial_coefficient(d_start, d_end):
    global d, n
    d *= d_start - d_end + 1
    n *= d_end

    if d % n == 0 and (d // n) % 2 == 0:
        return 1
    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N = int(input()) # 입력받은 정수
    if N == 0 or N == 1:
        print(0)
        continue
    cnt = 0
    end = N // 2
    for i in range(1, end):
        cnt += get_binomial_coefficient(N, i)
    cnt *= 2

    if N % 2 == 0:
        cnt +=  get_binomial_coefficient(N, N//2)
    print(cnt)


print(time.time() - start)

