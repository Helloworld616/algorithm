import sys
sys.stdin = open('input.txt')


# # 5. 서브 트리의 크기를 구하는 함수
# def count(n):
#     global cnt
#
#     for i in tree[n]:
#         # print(i)
#         # 자식노드의 개수만큼 카운팅해준다.
#         cnt += 1
#         cnt_list.append(i)
#
#     # 카운트 리스트에 자식 노드들을 넣어주고 하나씩 빼면서 그 노드의 자식노드들을 append 한다.
#     # print(tree[n][0])
#         n = cnt_list.pop()
#         # 자식노드에 연결된 노드들이 없다면 종료한다.
#         if tree[n][0]:
#             count(n)
#     return cnt

# 트리를 순회하면서 크기를 구하는 함수
def traversal(idx, cnt):
    # 한 번 순회할 때마다 크기에 1을 더한다.
    cnt[0] += 1
    # 만약 c_tree의 idx번째 노드가 자식을 가진다면
    if 0 not in tree[idx]:
        # 자식 노드로 내려가서 또 다시 탐색을 수행한다.
        for i in range(len(tree[idx])):
            traversal(tree[idx][i], cnt)


T = int(input())
for tc in range(1, 10):
    V, E, n1, n2 = map(int, input().split())
    # 0 두개로 채워주는 트리
    tree = [[0 for _ in range(2)] for _ in range(V+1)]
    node = list(map(int, input().split()))

    # 1. 트리가 비어있으면 부모 자식 정점을 이어주고 있다면 값을 추가해줌
    for i in range(E*2):
        if i % 2 == 0:
            if tree[node[i]] == [0, 0]:
                tree[node[i]] = [node[i+1]]
            else:
                tree[node[i]] += [node[i+1]]

    # 2-1. 빈 리스트에 첫번째 정점의 조상들을 넣어준다.
    anc_node1 = []
    while True:
        for i in range(len(tree)):
            if n1 in tree[i]:
                anc_node1 += [i]
                n1 = i
        if n1 == 1:
            break
    # print(anc_node1) # [5, 3, 1]

    # 2-2. 빈 리스트에 두번째 정점의 조상들을 넣어준다.
    anc_node2 = []
    while True:
        for i in range(len(tree)):
            if n2 in tree[i]:
                anc_node2 += [i]
                n2 = i
        if n2 == 1:
            break
    # print(anc_node2) # [11, 6, 3, 1]


    # 3. 두 정점의 공통조상을 찾아준다.
    same_anc = []
    if len(anc_node1) >= len(anc_node2):
        for i in anc_node2:
            if i in anc_node1:
                same_anc.append(i)
    else:
        for i in anc_node1:
            if i in anc_node2:
                same_anc.append(i)

    cnt_list = []
    # 처음으로 만나는 공통조상은 가장 앞의 값이다.
    n = same_anc[0]
    cnt = [0]
    # print(tree)
    print(same_anc)
    # 4. 가장 앞에 있는 공통조상의 서브트리의 크기를 구하는 함수를 실행한다.
    traversal(n, cnt)

    # 6. 결과값을 출력한다.
    print(f'#{tc} {same_anc[0]} {cnt[0]}')