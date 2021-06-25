a = "xababcdcdababcdcd"

cut = 1
answer = []
while cut < len(a):
    res = ''
    b=[]
    for i in range(0,len(a),cut):
        b.append(a[i:i+cut])

    count = 1
    for j in range(1,len(b)+1):

        if j == len(b):
            if count != 1:
                res += str(count) + b[j-1]
            else:
                res += b[j-1]
            continue
        if b[j-1] == b[j]:
            count += 1
        else:
            if count == 1:
                res += b[j-1]
            else:
                res += str(count)+b[j-1]
            count = 1
    cut += 1
    answer.append(len(res))

print(min(answer))