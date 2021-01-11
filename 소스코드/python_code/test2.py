from itertools import combinations

orders = ["AB", "BA", "CDBEA", "EFB", "EBF", "GG"]
course = [2,3,4]

result = list()

idx = 0
while True:
    if idx >= len(course):
        break
    size = course[idx]
    count = dict()
    for order in orders:
        order = list(order)
        temps = list(combinations(order,size))
        for temp in temps:
            temp = sorted(list(temp))
            temp = "".join(temp)
            if len(count) == 0:
                count[temp] = 1
            else:
                temp_reverse = temp[::-1]  # 거꾸로 뒤집어보기
                word = temp if temp < temp_reverse else temp_reverse
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
    count = dict(sorted(count.items(), key=(lambda x: x[1]), reverse=True))
    max = 2
    for key,value in count.items():
        if max <= value:
            max = value
            result.append(key)
        else:
            break

    idx += 1

result = sorted(result)
print(result)


