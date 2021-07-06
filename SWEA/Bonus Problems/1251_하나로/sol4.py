# 교수님 해설

import sys
sys.stdin = open("input.txt")


def get_distance(i1, i2):
    # root 씌워도 나중에 결국 제곱 함
    return abs(i1[0] - i2[0]) ** 2 + abs(i1[1] - i2[1]) ** 2


class DisjointSet:  # 존재이유 == 정점들끼리 이어져 있는지만을 확인하는 용도
    def __init__(self, n):
        self.parents = list(range(n))  # 최초는 자기 자신을 parent 로 가짐.
        self.ranks = [0 for _ in range(n)]  # union by rank 로 depth 를 줄이기 위해 사용

    # find root + path compression(특정 노드의 부모 노드 정보를 root 노드로 갱신)
    def find_root(self, node):
        parent = self.parents[node]
        if node != parent:  # root node 가 아니라면
            # '부모 노드' => '부모 노드의 부모 노드' 로 재귀적 갱신
            self.parents[node] = self.find_root(parent)
        return self.parents[node]

    # union by rank (rank == 내 밑에 몇세대가 있는지.)
    def union(self, node_v, node_u):
        root1 = self.find_root(node_v)
        root2 = self.find_root(node_u)

        # root1 rank 가 더 크거나 같다면, root2 를 root1 에 편입
        if self.ranks[root1] >= self.ranks[root2]:
            self.parents[root2] = root1
            # rank 가 같다면 임의로 하나를 잡아서 root 로 만들고, rank += 1
            if self.ranks[root1] == self.ranks[root2]:
                self.ranks[root1] += 1
        # root2 의 랭크가 더 크다면, 반대로.
        else:
            self.parents[root1] = root2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    coords = [[xs[idx], ys[idx]] for idx in range(N)]
    E = float(input())
    adj_matrix = [[get_distance(coords[i], coords[j]) for i in range(N)] for j in range(N)]
    djs = DisjointSet(N)

    edges = []

    for i in range(N):
        for j in range(i+1, N):  # 무방향 그래프기 때문에, 반쪽만 저장
            w = adj_matrix[i][j]
            edges.append((w, i, j))
    edges.sort()

    ans = 0
    for w, v, u in edges:
        root_v, root_u = djs.find_root(v), djs.find_root(u)
        # root 가 다르다면 == 한 가족이 아니라면 == cycle 이 만들어지지 않는다면,
        if root_v != root_u:
            djs.union(root_v, root_u)
            ans += w

    ans = ans * E
    print(f'#{tc} {round(ans)}')
