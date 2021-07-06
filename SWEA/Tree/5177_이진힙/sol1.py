import sys
from collections import deque
sys.stdin = open('sample_input.txt')


# 부모 노드와 비교/swap하는 함수
# 재귀를 통해 결국 모든 조상 노드들과 비교/swap하게 된다.
def heap_swap(tree, idx):
    # 현재 노드의 인덱스가 1보다 크고, 값이 부모 노드보다 작을 경우
    if idx > 1 and tree[idx] < tree[idx//2]:
        # 부모 노드와 현재 노드를 swap
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        # 한 단계 더 위의 부모 노드로 이동
        heap_swap(tree, idx//2)


# 조상 노드들의 합을 구하는 함수
# 재귀를 통해 조상 노드들을 계속 탐색하며
# 탐색한 조상 노드의 값을 결과값에 더한다.
def ancestor_sum(idx, ans):
    # idx가 0보다 클 경우에 탐색 및 합산 수행
    if idx > 0:
        # 조상 노드의 값을 결과값에 합산
        ans[0] += tree[idx]
        # 다음 조상 노드로 이동
        ancestor_sum(idx//2, ans)


# main
T = int(input())
for tc in range(1, T+1):
    # 노드의 갯수 입력 받기
    N = int(input())
    # 큐를 생성해 노드를 담는다.
    queue = deque(map(int, input().split()))

    # 트리 생성 후 초기화
    tree = [0] * (N+1)
    # 힙의 인덱스를 1로 초기화
    idx = 1

    # queue에서 노드를 차례대로 꺼낸 뒤 트리에 할당
    # 할당 후에는 조상 노드들과 값을 비교하여, 조상 노드 보다 값이 작을 경우 swap한다.
    while queue:
        # 트리에 노드 할당
        tree[idx] = queue.popleft()
        # 조상 노드들과 비교/swap 시행
        heap_swap(tree, idx)
        # 다음 인덱스로 이동
        idx += 1

    # 마지막 노드의 조상 노드들에 저장된 정수의 합 구하기
    ans = [0]
    ancestor_sum(N//2, ans)

    # 결과 출력
    print('#{} {}'.format(tc, ans[0]))


