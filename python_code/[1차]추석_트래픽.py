
def calcTime(h,m,s, T):
    h, m, s, T = int(h), int(m), float(s), float(T) #형변환
    if s < T: #s=00.464 T=1.466과 같은 경우
        m -= 1
        if m < 0:
            m = 59
            h -= 1
        s += 60.0

    return [h, m, round(s-T+0.001,3)]


# 1초 뒤 시간을 구함
def getAfter(time):
    h,m,s = time
    r_h, r_m, r_s = h, m, round(s + 1.000 - 0.001,3) # before_hour, before_min, before_sec
    if r_s >= 60.0:
        r_m += 1
        r_s -= 60.0
    if r_m >= 60:
        r_h += 1
        r_m -= 60
    return [r_h, r_m, r_s]

# 1초 전 시간을 구함
def getBefore(time):
    h, m, s = time
    r_h, r_m, r_s = -1, -1, -1.00
    r_h, r_m = h, m
    if s < 1.00:
        r_s = round(s + 60 - 1.000 + 0.001,3)
        r_m -= 1
        if r_m < 0:
            r_h -= 1
            r_m += 60
    else:
        r_s = round(s - 1.000 + 0.001, 3)
    return [r_h, r_m, r_s]

def compare(t1, t2):
    #t1 = [h, m, s], t2 = [h,m,s] 리스트로 들어온 시간의 대소를 비교
    # t1이 더 작으면 True를 리턴

    h1, m1, s1 = t1 #21 0 0.464
    h2, m2, s2 = t2 #20 59 58.233

    if h1 < h2:
        return True
    if h1 == h2 and m1 < m2:
        return True
    if h1 == h2 and m1 == m2 and s1 < s2:
        return True
    return False

def solution(lines):
    answer = 0
    traffic = list()
    for i in range(len(lines)):
        date, time, T = lines[i].split(' ')
        T = T[:-1] #뒤의 s 제거
        h, m, s = time.split(':')
        traffic.append([calcTime(h,m,s,T),[int(h),int(m),round(float(s),3)]])

    timestamp = list() #기준 시간대별로 앞 뒤로 1000ms 간격을 모두 timestamp에 저장함
    for i in range(len(traffic)):
        timestamp.append([getBefore(traffic[i][0]), traffic[i][0]])
        timestamp.append([traffic[i][0], getAfter(traffic[i][0])])

        timestamp.append([getBefore(traffic[i][1]), traffic[i][1]])
        timestamp.append([traffic[i][1],getAfter(traffic[i][1])])


    while timestamp:
        s, e = timestamp.pop(0) #start, end
        cnt = 0
        for i in range(len(traffic)):
            if compare(traffic[i][1],s) or compare(e, traffic[i][0]):
                continue
            cnt += 1

        if answer < cnt:
            answer = cnt

    return answer

print(solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"])) #1
print(solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"])) #2

#7
print(solution(["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s","2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s","2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s","2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s","2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]))