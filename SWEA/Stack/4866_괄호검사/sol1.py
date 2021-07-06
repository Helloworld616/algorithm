import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    cnt = 0
    for char in string:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
            cnt += 1
        if char == ')':
            if len(stack) > 0 and stack[len(stack)-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                cnt += 1
                break
        if char == ']':
            if len(stack) > 0 and stack[len(stack)-1] == '[':
                stack.pop()
            else:
                stack.append(char)
                cnt += 1
                break
        if char == '}':
            if len(stack) > 0 and stack[len(stack)-1] == '{':
                stack.pop()
            else:
                stack.append(char)
                cnt += 1
                break
    if cnt > 0:
        if len(stack) > 0:
            print('#{} {}'.format(tc, 0))
        else:
            print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
