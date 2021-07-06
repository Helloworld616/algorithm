# PASS

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


# 트리를 검사하는 함수
def is_tree():
    # 루트 존재 여부를 False로 초기화
    is_root = False

    for i in range(1, len(tree)):
        # 이미 루트가 존재하는데 진입 노드가 0개인 노드가 또 존재한다면 트리가 아님
        if is_root and node_check[i] and len(tree[i]) == 0:
            return False
        # 루트가 존재하지 않는 상황에서 진입 노드가 0개인 노드가 나왔다면
        # 루트 존재 여부를 True로 변경
        if not is_root and node_check[i] and len(tree[i]) == 0:
            is_root = True
        # 진입 노드가 1개보다 많으면 트리가 아님
        if node_check[i] and len(tree[i]) > 1:
            return False

    # 루트가 존재하지 않으면 트리가 아님
    if not is_root:
        return False

    # 위의 조건들을 모두 통과할 경우 트리!
    return True


# main
k = 1

# -1, -1이 나올 때까지 입력 받아서 트리 검사
while True:
    nodes = []  # 트리의 노드들을 담을 리스트 nodes
    is_end = False  # 마지막 케이스인지 체크하는 flag 변수

    # 마지막에 0, 0이나 -1, -1이 나올 때까지 입력 받기
    while True:
        # 입력 받은 수를 공백으로 구분한 리스트 numbers로 받기
        numbers = list(map(int, input().split()))
        # numbers의 길이가 0보다 크고, 마지막 두 원소가 0, 0일 때
        # nodes에 numbers를 추가하고 입력 종료
        if len(numbers) != 0 and numbers[-1] == 0 and numbers[-2] == 0:
            nodes.extend(numbers)
            break
        # numbers의 길이가 0보다 크고, 마지막 두 원소가 -1, -1일 때
        # 프로그램 종료
        if len(numbers) != 0 and numbers[-1] == -1 and numbers[-2] == -1:
            sys.exit(0)
        # 입력이 아무것도 없으면 다음 입력으로 건너뛰기
        if len(numbers) == 0:
            continue
        # nodes에 입력 받은 numbers를 추가
        nodes.extend(numbers)

    tree = [[] for _ in range(max(nodes) + 1)]  # 트리를 생성할 리스트
    node_check = [False for _ in range(max(nodes) + 1)]  # 노드의 유효성을 검사할 리스트

    # 각 노드의 진입 노드를 기록
    # 유효한 노드는 node_check의 값을 True로 변경
    for i in range(0, len(nodes) - 1, 2):
        tree[nodes[i + 1]].append(nodes[i])
        node_check[nodes[i]] = True
        node_check[nodes[i + 1]] = True

    # tree의 길이가 1이거나 (공백 트리이거나)
    # tree의 요건을 충족하면 트리임을 출력
    if len(tree) == 1 or is_tree():
        print(f'Case {k} is a tree.')
    # 아닐 경우 트리가 아님을 출력
    else:
        print(f'Case {k} is not a tree.')

    # 트리 검사가 끝나면 k의 값 1 증가
    k += 1

