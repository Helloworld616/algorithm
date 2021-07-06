# 오답


def cal(scores, expression):
    operand = ''
    operand_stack = []
    operator_stack = []
    expression_list = list(expression)

    for char in expression_list:
        if char.isdigit():
            operand += char
        else:
            operand_stack.append(int(operand))
            operand = ''
            if len(operator_stack) != 0:
                if scores[operator_stack[-1]] >= scores[char]:
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()

                    if operator == '*':
                        operand_stack.append(operand1 * operand2)
                    if operator == '+':
                        operand_stack.append(operand1 + operand2)
                    if operator == '-':
                        operand_stack.append(operand1 - operand2)

            operator_stack.append(char)

    operand_stack.append(int(operand))

    minus_stack = []
    while operator_stack:
        operator = operator_stack.pop()

        if operator == '-':
            if not len(minus_stack):
                minus_stack.append(operand_stack.pop())
                minus_stack.append(operand_stack.pop())
            else:
                minus_stack.append(operand_stack.pop())
        else:
            if len(minus_stack):
                while len(minus_stack) != 1:
                    minus_stack.append(minus_stack.pop() - minus_stack.pop())
                operand_stack.append(minus_stack.pop())
            if operator == '*':
                operand_stack.append(operand_stack.pop() * operand_stack.pop())
            if operator == '+':
                operand_stack.append(operand_stack.pop() + operand_stack.pop())

    if len(minus_stack):
        while len(minus_stack) != 1:
            minus_stack.append(minus_stack.pop() - minus_stack.pop())
        operand_stack.append(minus_stack.pop())

    return operand_stack[0]


def perm(result, operators, scores, expression, depth, visited):
    if depth == 3:
        result.append(abs(cal(scores, expression)))

    else:
        for i in range(3):
            if not visited[i]:
                scores[operators[depth]] = i
                visited[i] = True
                perm(result, operators, scores, expression, depth + 1, visited)
                visited[i] = False


def solution(expression):
    result = []
    operators = ['*', '+', '-']
    scores = {'*': 0, '+': 0, '-': 0}
    visited = [False] * 3
    perm(result, operators, scores, expression, 0, visited)

    return max(result)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))