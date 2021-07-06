import sys
sys.stdin = open('sample_input.txt')


def solution(string):
    result = 1
    stack = []
    openers = ['(', '{', '[']
    closers = [')', '}', ']']
    for char in string:
        if char in openers:
            stack.append(char)
        if char in closers:
            # 닫는 괄호가 나왔는데, stack이 비어있다면(opener < closer)
            if not len(stack):
                result = 0
                break
            # 닫는 괄호와 마지막 열린 괄호의 짝이 맞지 않다면
            else:
                if char == ')' and stack.pop() != '(':
                    result = 0
                    break
                elif char == '}' and stack.pop() != '{':
                    result = 0
                    break
                elif char == ']' and stack.pop() != '[':
                    result = 0
                    break
        # string이 끝났는데, stack이 남아있다면(opener > closer)
        else:
            if len(stack):
                result = 0

        return result


T = int(input())
for tc in range(1, T+1):
    code = input()
    print("#{} {}".format(tc, solution(code)))
