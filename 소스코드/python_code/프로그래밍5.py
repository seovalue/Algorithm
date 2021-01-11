import datetime
def solution(totalTicket, logs):
    answer = []
    process = [] #로그가 진행되는 과정을 담을 스택
    for log in logs:
        id, action, time_str = log.split(' ') #띄어쓰기 기준 분리
        time = datetime.datetime.strptime(time_str, '%H:%M:%S')

        ## 예외 처리 ##
        if time < datetime.datetime(1900,1,1,9,0,0): #오전 9시 이전의 경우에는
            continue
        if action == 'request' and time == datetime.datetime(1900,1,1,10,0,0): #10:00:00에 접속했으면 종료이므로 continue
            continue

        if action == 'request':
            if process:
                id1, action1, time1 = process.pop()
                if (time - time1).seconds >= 60:
                    answer.append(id1)
                else:
                    if id1 != id: #id가 다른데 60초 차이가 안나는 경우 (동접이므로 id의 접속자는 접속 불가)
                        process.append([id1, action1, time1])  #또한 기존 접속자를 계속 배열에 유지!
                        continue
            process.append([id, action, time])

        if action == 'leave':
            id1, action1, time1 = process.pop() #맨 뒤의 것을 가져옴.
            if id1 == id and (time - time1).seconds >= 60: #id가 같고 1초보다 크면
                answer.append(id)

        if len(answer) > totalTicket: #전체 티켓의 개수보다 넘어선 경우
            answer = sorted(answer)
            return answer

    if process: #남아있는 로그의 경우에는 answer에 추가해준다.
        answer.append(process[-1][0])
    answer = sorted(answer)
    return answer

# 접속 시도를 하면 request로그가 남고, 1분 이내 접속을 종료하면 leave
# 티켓 구매를 위해서는 서버 접속 1분을 유지
# 이미 한 유저가 접속한 상태면 다른 유저는 접속할 수 없다.
# 티켓 구매를 성공한 유저는 접속은 가능하되 다시 구매는 불가능


logs =  [
    "woni request 09:12:29",
    "brown request 09:23:11",
    "brown leave 09:23:44",
    "jason request 09:33:51",
    "jun request 09:33:56",
    "cu request 09:34:02"
]

print(solution(2000, logs))
'''
[
    "jason",
    "woni"
]
'''

logs =  [
    "a request 08:59:59",
    "b request 09:00:00",
    "b leave 09:01:00",
    "c request 09:01:00",
    "d request 09:02:00",
    "e request 09:04:00",
    "f request 09:04:59"
]

print(solution(2000, logs))

