import sys
import itertools

sys.stdin = open("input.txt","rt")
n, m = map(int,sys.stdin.readline().split())
home = []
chicken = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j, k in enumerate(temp):
        if k == 1: #값이 1인경우는 집
            home.append([i,j])
        elif k == 2: #값이 2인 경우는 치킨집
            chicken.append([i,j])

final_chicken_distance = 99999 #가장 최종 치킨 거리 값
for select_chicken in itertools.combinations(chicken,m):
    total_chicken_distance = 0 # m개의 조합으로 꾸려질 치킨집들의 치킨 거리 합
    for h_loc in home:
        chick_dist = 99999
        for c_loc in select_chicken: # 선택된 m개의 치킨 집들과, 집 간의 거리를 측정함.
            distance = abs(h_loc[0] - c_loc[0]) + abs(h_loc[1] - c_loc[1])
            chick_dist = chick_dist if distance > chick_dist else distance
        total_chicken_distance += chick_dist #각 집들과 선택된 m개의 집들 중 치킨 거리가 최소인 치킨 거리를 total 에 더함.
    final_chicken_distance = final_chicken_distance if final_chicken_distance < total_chicken_distance else total_chicken_distance

print(final_chicken_distance)