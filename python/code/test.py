new_id ="abcdefghijklmn.p"

allow = ['-','_','.']
#1단계
new_id = new_id.lower()
res_id = []

#2단계
for word in new_id:
    if word in allow or 97 <= ord(word) <= 122 or word.isdigit():
        res_id.append(word)

#3단계
dot = 0
i = 0
while True:
    if i >= len(res_id):
        break
    if res_id[i] == '.':
        dot += 1
        if dot >= 2:
            res_id.pop(i)
            i -= 1
            dot -= 1
    else:
        dot = 0
    i += 1

#4단계
if res_id and res_id[0] == '.':
    res_id.pop(0)
if res_id and res_id[-1] == '.':
    res_id.pop()

#5단계
if not res_id:
    res_id.append("a")

#6단계
if len(res_id) >= 16:
    res_id = res_id[:15]
    if res_id[-1] == '.':
        res_id.pop()

#7단계
last_word = res_id[-1]
while len(res_id) < 3:
    res_id.append(last_word)

print("".join(res_id))



