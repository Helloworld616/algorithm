import sys
sys.stdin = open('input.txt')


# 후위순회 함수
def postorder(idx):
    # 인덱스가 None이 아니면 수행
    if idx:
        # 왼쪽 자식 순회
        postorder(tree[idx][1])
        # 오른쪽 자식 순회
        postorder(tree[idx][2])

        # 노드의 값 체크
        # 1. 값이 연산자일 경우 스택에서 숫자 두 개를 꺼낸 뒤 연산 수행
        if tree[idx][0] == '+':
            stack.append(stack.pop() + stack.pop())
        elif tree[idx][0] == '-':
            # 뺄셈일 때는 피연산자의 순서가 중요하므로 숫자를 따로 변수에 할당
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)
        elif tree[idx][0] == '*':
            stack.append(stack.pop() * stack.pop())
        elif tree[idx][0] == '/':
            # 나눗셈일 때도 피연산자의 순서가 중요하므로 숫자를 따로 변수에 할당
            second = stack.pop()
            first = stack.pop()
            stack.append(first / second)
        # 2. 값이 피연산자일 경우 스택에 담는다.
        else:
            stack.append(tree[idx][0])


# main
T = 10
for tc in range(1, T+1):
    # 노드의 갯수 입력받기
    N = int(input())
    # 트리 생성 및 초기화
    tree = [[0 for _ in range(3)] for _ in range(N+1)]

    # 입력 정보를 트리에 할당
    for _ in range(N):
        # 입력 정보를 노드에 할당
        node = input().split()

        # 노드의 원소 중 숫자인 것은 자료형을 정수로 변환
        for i in range(len(node)):
            if node[i].isdigit():
                node[i] = int(node[i])
        # 자식이 없는 노드는 자식을 None으로 채워줌
        # 이렇게 하는 이유는 후위순회를 편하게 하기 위함이다!
        node += [None] * (4-len(node))

        # 노드의 0번째 원소를 트리의 인덱스로 할당
        idx = node[0]
        # 기존의 노드는 1부터 마지막 인덱스까지 슬라이싱
        node = node[1:]
        # 트리에 노드를 할당
        tree[idx] = node

    # 연산을 수행하기 위한 스택 생성
    stack = []
    # 후위순회 시행
    postorder(1)

    # 결과 출력
    print('#{} {}'.format(tc, int(stack[0])))