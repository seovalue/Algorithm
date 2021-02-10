import sys

sys.stdin = open("input.txt", "rt")

T = int(input())  # 전체 테스트 케이스의 수
SANGWON = 1
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    relation = [[0] * (n + 1) for _ in range(n + 1)]

    # 관계 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        relation[a][b] = 1
        relation[b][a] = 1

    invitation = set()
    close_friends = list()

    # 상원이의 친한 친구를 초대장 목록에 추가
    for idx, rel in enumerate(relation[SANGWON]):
        if rel == 1:
            invitation.add(idx)
            close_friends.append(idx)

    for f in close_friends:
        for idx, rel in enumerate(relation[f]):
            if rel == 1:
                invitation.add(idx)

    answer = len(invitation)
    if len(invitation) > 0:
        answer -= 1

    print("#{} {}".format(test_case, len(invitation)))
