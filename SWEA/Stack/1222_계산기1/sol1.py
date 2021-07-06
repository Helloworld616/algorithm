import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    formula = input()
    
    # 후위 표기식 만들기
    postfix = ''
    numbers = '0123456789'
    n_stack = []
    p_stack = []
    for char in formula:
        if char in numbers:
            if not len(p_stack):
                n_stack.append(char)
            else:
                if not len(n_stack):
                    postfix += char + p_stack.pop()
                else:
                    postfix += n_stack.pop() + char + p_stack.pop()
        else:
            p_stack.append(char)
    # print(postfix)

    # 후위 표기식 계산하기
    total = 0
    for char in postfix:
        if char in numbers:
            n_stack.append(char)
        else:
            if len(n_stack) > 1:
                total += int(n_stack.pop()) + int(n_stack.pop())
            else:
                total += int(n_stack.pop())

    print('#{} {}'.format(tc, total))



