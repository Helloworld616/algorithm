import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    formula = input()
    numbers = '1234567890'
    score = {'+': 0, '*': 1}
    stack = []

    postfix = ''
    for char in formula:
        if char in numbers:
            postfix += char
        elif len(stack) == 0 or score[stack[len(stack)-1]] < score[char]:
            stack.append(char)
        else:
            while stack:
                if score[stack[len(stack)-1]] < score[char]:
                    break
                postfix += stack.pop()
            stack.append(char)
    if stack:
        while stack:
            postfix += stack.pop()

    for char in postfix:
        if char in numbers:
            stack.append(char)
        elif char == '*':
            result = int(stack.pop()) * int(stack.pop())
            stack.append(result)
        else:
            result = int(stack.pop()) + int(stack.pop())
            stack.append(result)

    print('#{} {}'.format(tc, stack.pop()))






