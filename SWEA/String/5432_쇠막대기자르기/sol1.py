import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    idx = 0
    total = 0
    while idx <= len(string)-1:
        if string[idx:idx+2] == '()' and len(stack) > 0:
            for i in range(len(stack)):
                stack[i] += 1
            idx += 2
        else:
            if string[idx] == '(' and string[idx+1] != ')':
                stack.append(0)
            elif string[idx] == ')' and len(stack) > 0:
                total += stack.pop() + 1
            idx += 1
    print('#{} {}'.format(tc, total))


