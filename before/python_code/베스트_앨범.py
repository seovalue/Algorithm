from operator import attrgetter
# 장르별 재생횟수 합을 구하는 함수
def play_sum(li):
    total = 0
    for i in range(len(li)):
        total += li[i][1]
    return total

def get_top_2(li):
    li = sorted(li,key = lambda x:x[1], reverse=True)
    top1, top2 = li[0][0], li[1][0]
    return top1, top2


def solution(genres, plays):
    answer = []
    unique_genres = set(genres)  # 장르명에서 중복된 것 제외

    genres_plays = dict() # {"장르명":[인덱스, 재생횟수]}
    for i in range(len(genres)):
        if genres[i] in genres_plays.keys():
            genres_plays[genres[i]].append([i,plays[i]])
        else:
            genres_plays[genres[i]] = [[i, plays[i]]]

    genres_plays_sum = dict() #{"장르명":총 재생 횟수}
    for genre in unique_genres:
        li = genres_plays[genre]
        genres_plays_sum[genre] = play_sum(li) #장르별 재생횟수 합을 value로 가짐.

    # 재생횟수 합이 큰 순으로 정렬
    genres_plays_sum = sorted(genres_plays_sum.items(), key=(lambda x:x[1]), reverse=True)
    for g in genres_plays_sum:
        if len(genres_plays[g[0]]) == 1:
            answer.append(genres_plays[g[0]][0][0])
        else:
            a,b = get_top_2(genres_plays[g[0]])
            answer.append(a)
            answer.append(b)

    return answer


genres = ["classic", "classic", "classic", "classic", "pop"]
plays=[500,150,800,800,2500]
print(solution(genres,plays))


