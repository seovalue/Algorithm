from itertools import combinations

def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    cases = list(combinations(nums, 3))
    count = 0
    for case in cases:
        if isPrime(sum(case)):
            count += 1
    return count