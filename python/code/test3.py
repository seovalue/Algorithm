def solution(info, query):

    answer = []
    info_list = list()
    for item in info:
        info_list.append(list(map(str,item.split())))

    query_list = list()
    for q in query:
        query_list.append(list(map(str,q.split())))

    for q in query_list:
        i = 0
        while True:
            if i >= len(q): break
            if q[i] == 'and':
                q.pop(i)
                i -= 1
            i += 1


    for query in query_list:
        total = 0
        # 알맞은 사람 찾기
        for info in info_list:
            cnt = 0
            if '-' in query:
                for i in range(len(query)-1):
                    if query[i] == '-':
                        cnt += 1
                    elif query[i] != info[i]:
                        break
                    else:
                        cnt += 1
                if int(query[4]) <= int(info[4]):
                    cnt += 1
                if cnt == 5:
                    total += 1
            else:
                if query[:4] == info[:4] and int(query[4]) <= int(info[4]):
                    total += 1
        answer.append(total)

    return answer