import sys
sys.stdin = open('sample_input.txt')


T = int(input())


for tc in range(1, T+1):
    string = input()
    stack = [string[0]]
    for i in range(1, len(string)):
        if len(stack) > 0 and string[i] == stack[len(stack)-1]:
            stack.pop()
        else:
            stack.append(string[i])
    print('#{} {}'.format(tc, len(stack)))


