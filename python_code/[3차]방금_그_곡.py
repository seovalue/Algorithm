import datetime
def solution(m, musicinfos):
    answer = ['',0]
    mm = []
    for c in m:
        if c == '#':
            mm.append(mm.pop() + c)
        else:
            mm.append(c)
    mt = ''.join(mm)
    musicinfos = [x.split(',') for x in musicinfos]
    for info in musicinfos:
        t1 = datetime.datetime.strptime(info[0], '%H:%M')
        t2 = datetime.datetime.strptime(info[1], '%H:%M')
        dt = ((t2 - t1).seconds)//60
        music = []
        for mu in info[3]:
            if mu == '#':
                music.append(music.pop() + mu)
            else:
                music.append(mu)
        else:
            if dt < len(music):
                music = music[:dt]
            else:
                music = music*(dt//len(music)) + music[:(dt%len(music))]
            for i in range(len(music) - len(mm) + 1):
                if ''.join(music[i:i+len(mm)]) == mt and dt > answer[1]:
                    answer = [info[2], dt]
    if answer[1]:
        return answer[0]
    return '(None)'

print(solution("A#",["23:56,00:00,HAPPY,B#A#"]))
print(solution("CDEFGAC",["12:00,12:06,HELLO,CDEFGA"])) #none
print(solution("CCB",["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])) #foo

import datetime


def solution(m, musicinfos):
    answer = ['', 0]  # 타이틀, 재생시간

    # #이 들어있는 것은 하나로 합쳐준다.
    m_list = []
    for m1 in m:
        if m1 == '#':
            m_list.append(m_list.pop() + m1)
        else:
            m_list.append(m1)
    m = ''.join(m_list)

    musicinfos = [x.split(',') for x in musicinfos]

    for info in musicinfos:  # info = [시작시간, 끝시간, 제목, 멜로디]
        start = datetime.datetime.strptime(info[0], '%H:%M')
        end = datetime.datetime.strptime(info[1], '%H:%M')
        dt = ((end - start).seconds) // 60

        melody = list()
        for mu in info[3]:
            if mu == '#':
                melody.append(melody.pop() + mu)
            else:
                melody.append(mu)
        else:
            # 멜로디의 길이가 주어진 시간보다 길다면
            if dt < len(melody):
                melody = melody[:dt]
            else:
                melody = melody * (dt // len(melody)) + melody[:(dt % len(melody))]
            # m의 길이만큼 melody를 쪼개서, m과 동일한지 확인
            for i in range(len(melody) - len(m) + 1):
                # melody를 m의 길이만큼 쪼갠 것과 m이 같고, 재생 시간이 길다면
                if ''.join(melody[i:i + len(m)]) == m and dt > answer[1]:
                    answer = [info[2], dt]

        if answer[1]:
            return answer[0]
        else:
            return '(None)'