T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    stack = []
    string = 'xxyyzz'
    for s in string:
        if not stack:
            stack.append(s)
            continue
        top = stack[0]
        if top == s:
            stack.pop(0)
        else:
            stack.insert(0, s)

        print(stack)
    stack = ''.join(sorted(stack))
    print(string)