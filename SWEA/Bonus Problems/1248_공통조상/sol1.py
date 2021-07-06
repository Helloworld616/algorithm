import sys
sys.stdin = open('input.txt')


# 조상 노드들을 구하는 함수
def find_parents(idx, parents, dist):
    # 만약 p_tree의 idx번째 노드가 존재한다면
    if len(p_tree[idx]):
        # idx번째 노드의 조상 노드와 거리를 리스트에 추가한다.
        parents.append([p_tree[idx][0], dist])
        # 부모 노드로 올라가서 또 다시 탐색을 수행한다.
        find_parents(p_tree[idx][0], parents, dist+1)


# 트리를 순회하면서 크기를 구하는 함수
def traversal(idx, cnt):
    # 한 번 순회할 때마다 크기에 1을 더한다.
    cnt[0] += 1
    # 만약 c_tree의 idx번째 노드가 자식을 가진다면
    if len(c_tree[idx]):
        # 자식 노드로 내려가서 또 다시 탐색을 수행한다.
        for i in range(len(c_tree[idx])):
            traversal(c_tree[idx][i], cnt)


# main
T = int(input())
for tc in range(1, T+1):
    # 입력 받기
    V, E, F, S = map(int, input().split())
    edge = list(map(int, input().split()))
    
    # 부모 정보를 저장할 p_tree, 자식 정보를 저장할 c_tree 생성
    p_tree = [[] for _ in range(V + 1)]
    c_tree = [[] for _ in range(V + 1)]
    
    # 간선에서 주어지는 부모, 자식 연결 정보를 p_tree와 c_tree에 저장
    for i in range(0, len(edge), 2):
        p_tree[edge[i+1]].append(edge[i])
        c_tree[edge[i]].append(edge[i+1])

    # 첫 번째 노드의 조상 노드들 구하기
    f_parents = []
    find_parents(F, f_parents, 1)

    # 두 번째 노드의 조상 노드들 구하기
    s_parents = []
    find_parents(S, s_parents, 1)

    # 첫 번째 노드와 두 번째 노드의 공통 조상 노드들(ancestors) 구하기
    ancestors = []
    for fp in f_parents:
        for sp in s_parents:
            if fp[0] == sp[0]:
                ancestors.append(fp)

    # 조상 노드들 중 기준 노드와의 거리가 가장 짧은 조상 노드(ancestor) 구하기
    ancestor = ancestors[0][0]
    min_dist = ancestors[0][1]
    for i in range(1, len(ancestors)):
        if ancestors[i][1] < min_dist:
            ancestor = ancestors[0][0]

    # 조상 노드를 루트로 가지는 서브 트리의 크기 구하기
    cnt = [0]
    traversal(ancestor, cnt)

    # 결과 출력
    print('#{} {} {}'.format(tc, ancestor, cnt[0]))
