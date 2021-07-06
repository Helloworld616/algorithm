import sys
sys.stdin = open('sample_input.txt')

T = int(input())
operator = '+-/*'

for tc in range(1, T+1):
    sequence = input().split()
    sequence.pop()
    stack = []
    flag = True
    for char in sequence:
        if char in operator:
            if len(stack) < 2:
                flag = False
                break
            num2 = stack.pop()
            num1 = stack.pop()
            if char == '*':
                stack.append(num1 * num2)
            if char == '/':
                stack.append(num1 // num2)
            if char == '+':
                stack.append(num1 + num2)
            if char == '-':
                stack.append(num1 - num2)
        else:
            stack.append(int(char))

    if flag and len(stack) == 1:
        print('#{} {}'.format(tc, stack.pop()))
    else:
        print('#{} error'.format(tc))



