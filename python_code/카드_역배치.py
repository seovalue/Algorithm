# import sys
# sys.stdin = open("input.txt","rt")

cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for test_case in range(10):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    Slice = cards[a:b+1]
    tmp = cards[a:b+1]

    j = len(tmp)
    for i in range(len(Slice)):
        j -= 1
        Slice[i] = tmp[j]


    j = 0
    for i in range(a,b+1):
        cards[i] = Slice[j]
        j += 1


for card in cards:
    print(card, end= ' ')


