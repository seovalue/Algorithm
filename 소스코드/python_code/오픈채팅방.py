def make_result(records, id_nick):
    result = []
    for record in records:
        nickname = id_nick[record[1]]
        if record[0] == 'Enter':
            result.append(nickname + "님이 들어왔습니다.")
        elif record[0] == 'Leave':
            result.append(nickname + "님이 나갔습니다.")

    return result


def solution(record):
    answer = []

    record_list = []
    id_nick = {}

    for r in record:
        records = list(r.split()) #문자열을 띄어쓰기 기준 리스트로 변환
        if records[0] != 'Leave':
            id_nick[records[1]] = records[2]
        record_list.append(records)

    answer = make_result(record_list, id_nick)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))