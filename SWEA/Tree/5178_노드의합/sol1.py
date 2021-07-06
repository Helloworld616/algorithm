import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 노드의 개수, 리프 노드의 개수, 노드 번호 입력 받기
    N, M, L = map(int, input().split())

    # 트리 생성 및 초기화
    # 자식이 하나만 있는 경우도 포괄하기 위해 N+2를 곱함
    tree = [0] * (N + 2)
    # 리트 노드의 인덱스를 담을 리스트 leaf_idx 생성
    leaf_idx = []

    # 입력 정보를 받아 tree와 leaf_idx에 할당
    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num
        leaf_idx.append(idx)

    # 리프 노드부터 bottom-up 합산 시작
    # leaf_idx를 이용해 리프 노드들을 찾아낸 뒤 합산을 수행
    # 합산 값을 부모 노드에 할당한 후 부모 노드의 idx를 leaf_idx에 추가
    for idx in leaf_idx:
        # 부모 노드의 값이 0일 때에만 수행
        if not tree[idx//2]:
            # 인덱스가 홀수일 경우
            if idx % 2:
                # 현재 노드와 이전 노드 값의 합을 부모 노드에 할당
                tree[idx//2] = tree[idx] + tree[idx-1]
            # 인덱스가 짝수일 경우
            else:
                # 현재 노드와 다음 노드 값의 합을 부모 노드에 할당
                tree[idx // 2] = tree[idx] + tree[idx+1]
            # leaf_idx에 부모 노드 추가
            leaf_idx.append(idx//2)

    # L번째 노드의 값 출력
    print('#{} {}'.format(tc, tree[L]))
