N = int(input())
clap = "-"
number_include = ['3', '6', '9']
answer = ''


def check(string, number):
    answer = ''
    for i in range(len(number)):
        count = string.count(number[i])
        if count > 0:
            answer += clap * count

    if not answer:
        answer += string
    return answer + " "


for i in range(1,N+1):
    answer += check(str(i), number_include)

print(answer)