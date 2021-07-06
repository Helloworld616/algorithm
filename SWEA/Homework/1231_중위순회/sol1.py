import sys
sys.stdin = open('input.txt')


# 중위 순회 함수
def inorder(idx, ans):
    # idx가 None이 아니면 순회 수행
    if idx:
        # 왼쪽 자식 순회
        inorder(tree[idx][1], ans)
        # 부모 노드의 값을 정답에 합산
        ans[0] += tree[idx][0]
        # 오른쪽 자식 순회
        inorder(tree[idx][2], ans)


# main
T = 10

for tc in range(1, T+1):
    # 정점의 총 갯수 입력 받기
    N = int(input())

    # 트리 생성 및 초기화
    tree = [0] * (N+1)

    # 입력으로 들어오는 정보들을 트리에 넣는다.
    for i in range(N):
        # 입력을 리스트 node로 변환
        node = input().split()

        # node의 정보 중 숫자인 것은 자료형을 정수로 변경
        for j in range(len(node)):
            if node[j].isdigit():
                node[j] = int(node[j])

        # 자식이 없는 노드는 자식 노드를 None으로 채워준다. (중위 순회를 편하게 하기 위함임)
        node += [None] * (4 - len(node))

        # node의 0번째 값을 idx로 할당하고
        idx = node[0]
        # 기존의 node를 1번째 인덱스부터 마지막 인덱스까지 슬라이스 해준다.
        node = node[1:]

        # tree의 idx에 node를 할당한다.
        tree[idx] = node

    # 정답을 담은 리스트 ans 생성
    ans = ['']
    # 루트 노트부터 중위 순회 시행
    inorder(1, ans)

    # 결과 출력
    print('#{} {}'.format(tc, ans[0]))
