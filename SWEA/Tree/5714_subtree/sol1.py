import sys
sys.stdin = open('sample_input.txt')


# 트리를 순회하는 함수
def traversal(idx, cnt):
    # 한 번 순회할 때마다 순회 횟수를 1 더함
    cnt[0] += 1
    # 자식이 존재하면 다음 순회를 실행
    if len(tree[idx]):
        # 연결된 자식 노드로 이동하여 순회
        for i in range(len(tree[idx])):
            traversal(tree[idx][i], cnt)


# main
T = int(input())

for tc in range(1, T+1):
    # 간선의 갯수와 루트 노드 입력 받기
    E, N = map(int, input().split())
    # 간선 정보 입력 받기
    edge = list(map(int, input().split()))

    # 트리 생성 후 초기화
    tree = [[] for _ in range(max(edge)+1)]

    # 트리의 부모 노드에 자식 노드를 연결
    for i in range(0, len(edge), 2):
        tree[edge[i]].append(edge[i+1])

    # 트리 순회 시행
    cnt = [0]
    traversal(N, cnt)

    print('#{} {}'.format(tc, cnt[0]))
