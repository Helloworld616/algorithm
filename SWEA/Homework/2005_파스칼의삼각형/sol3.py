# stack 사용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stack = []
    pascal = []
    temp = []

    for idx in range(N):
        pascal.append(1)
        temp.append(1)
        while 0 < idx:
            if len(stack) == 1:
                pascal.append(stack.pop())
                temp.append(pascal[len(pascal) - 1])
                break
            else:
                pascal.append(stack.pop() + stack[len(stack)-1])
                temp.append(pascal[len(pascal) - 1])
        stack += temp
        temp.clear()

    print('#{}'.format(tc))
    cut = 0
    increase = 2
    for i in range(len(pascal)):
        print('{}'.format(pascal[i]), end = ' ')
        if i == cut:
            print()
            cut += increase
            increase += 1


