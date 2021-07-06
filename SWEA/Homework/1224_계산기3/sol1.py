import sys
sys.stdin = open('input.txt')

icp = {'(': 3, '+': 1, '*': 2}
isp = {'(': 0, '+': 1, '*': 2}
numbers = '0123456789'

for tc in range(1, 11):
    N = int(input())
    sequence = input()
    postfix = ''
    stack = []
    for char in sequence:
        if char in numbers:
            postfix += char
        else:
            if char == ')':
                while stack[len(stack)-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            elif len(stack) == 0 or isp[stack[len(stack)-1]] < icp[char]:
                stack.append(char)
            elif isp[stack[len(stack)-1]] >= icp[char]:
                while len(stack) > 0 and isp[stack[len(stack)-1]] >= icp[char]:
                    postfix += stack.pop()
                stack.append(char)
    while stack:
        postfix += stack.pop()
    #print(postfix)

    for char in postfix:
        if char in numbers:
            stack.append(char)
        if char == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        if char == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))

    print("#{} {}".format(tc, stack.pop()))



