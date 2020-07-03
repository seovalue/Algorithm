# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
words = []
for i in range(n):
    words.append(input())

poem = []
for i in range(n-1):
    poem.append(input())

for word in words:
    if word not in poem:
        print(word)