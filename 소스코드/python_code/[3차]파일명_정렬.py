def distinguish(s):
    print(s)
    head = []
    number = []

    flag = False
    j = -1
    for i in range(len(s)):
        if not flag and s[i].isdigit():
            head.append(s[:i].lower())
            flag = True
            j = i
        if not s[i].isdigit() and j != -1:
            if i - j > 5:
                number.append(int(s[j:j+5]))
            else:
                number.append(int(s[j:i]))
            return head, number
        if j != -1 and i - j == 5:
            number.append(int(s[j:i]))
            return head, number

    number.append(int(s[j:i+1]))
    return head, number


def solution(files):
    answer = []
    new_files = []  # [HEAD, NUMBER, INDEX]
    for i in range(len(files)):
        head, number = distinguish(files[i])
        new_files.append([head, number, i])

    new_files = sorted(new_files, key=lambda x: (x[0], x[1], x[2]))  # 모두 오름차순
    for file in new_files:
        answer.append(files[file[2]])

    return answer

print(solution(["img000012345", "img1.png","img2","IMG02"]))