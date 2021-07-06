# PASS


# 상금 계산 함수
# 후위 표기식에서 원소를 하나씩 꺼내서 연산
def cal(postfix):
    # 스택 생성
    stack = []

    # 후위표기식 순회
    for char in postfix:
        # 원소가 숫자일 경우 바로 스택에 추가
        if char.isdigit():
            stack.append(int(char))
        # 원소가 곱셈일 경우 바로 곱셈 연산 후 결과값을 스택에 추가
        elif char == '*':
            result = stack.pop() * stack.pop()
            stack.append(result)
        # 원소가 덧셈일 경우 바로 덧셈 연산 후 결과값을 스택에 추가
        elif char == '+':
            result = stack.pop() + stack.pop()
            stack.append(result)
        # 원소가 뺄셈일 경우 바로 뺄셈 연산 후 결과값을 스택에 추가
        elif char == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 - num2
            stack.append(result)

    # 마지막에는 최종 결과값 하나만 스택에 남음
    # 결과값을 빼낸 뒤 절대값 연산 결과를 반환
    return abs(stack.pop())


# 후위표기식 변환 함수
def make_postfix(expression, scores):
    operand = ''  # 피연산자
    postfix = []  # 후위표기식 변환 결과
    stack = []  # 스택

    # 주어진 식에서 원소를 하나씩 꺼냄
    for char in expression:
        # 숫자일 경우 피연산자에 추가
        if char.isdigit():
            operand += char
        # 숫자가 아닐 경우
        # 1. 스택이 비어있거나, 들어오는 연산자가 스택의 마지막 연산자보다 우선 순위가 높을 경우
        elif len(stack) == 0 or scores[stack[-1]] < scores[char]:
            # 피연산자를 후위표기식에 추가 후 초기화
            postfix.append(operand)
            operand = ''
            # 들어오는 연산자를 스택에 추가
            stack.append(char)
        # 2. 이외의 경우 : 스택이 비어있지 않고, 들어오는 연산자가 스택의 마지막 연산자보다 우선 순위가 낮을 경우
        else:
            # 피연산자를 후위표기식에 추가 후 초기화
            postfix.append(operand)
            operand = ''
            # 스택의 마지막 연산자가 들어오는 연산자보다 우선 순위가 낮지 않을 때까지
            # 스택의 연산자를 빼내서 후위표기식에 추가
            while stack:
                if scores[stack[-1]] < scores[char]:
                    break
                postfix.append(stack.pop())
            # 들어오는 연산자를 스택에 추가
            stack.append(char)
    # 마지막 피연산자를 스택에 추가
    stack.append(operand)

    # 아직 스택에 값이 남아 있을 경우
    if stack:
        # 스택이 빌 때까지
        # 스택의 원소들을 하나씩 꺼내서 후위표기식에 추가
        while stack:
            postfix.append(stack.pop())

    # 후위표기식 반환
    return postfix


# 순열 생성 함수
def perm(result, operators, scores, expression, depth, visited):
    # 재귀의 깊이가 3이 될 때
    if depth == 3:
        # 주어진 식을 후위표기식으로 변환한 뒤 연산
        # 연산 결과를 결과 리스트에 추가
        postfix = make_postfix(expression, scores)
        result.append(cal(postfix))
    # 재귀의 깊이가 아직 3이 안 되었을 경우 재귀를 계속 수행
    else:
        # 0, 1, 2 중의 숫자들 안에서 우선 순위를 분배
        for i in range(3):
            # 방문 배열을 이용
            # 아직 방문하지 않은 숫자(사용하지 않은 숫자)일 경우
            if not visited[i]:
                # 현재 연산자의 점수에 넣고 다음 재귀 수행
                scores[operators[depth]] = i
                visited[i] = True
                perm(result, operators, scores, expression, depth + 1, visited)
                visited[i] = False


# 솔루션 함수
def solution(expression):
    result = []  # 결과 리스트
    operators = ['*', '+', '-']  # 피연산자 리스트
    scores = {'*': 0, '+': 0, '-': 0}  # 피연산자의 숫자를 담은 사전
    visited = [False] * 3  # 방문 배열
    perm(result, operators, scores, expression, 0, visited)  # 순열 탐색 및 결과 연산

    # 결과 리스트의 최대값을 반환
    return max(result)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))