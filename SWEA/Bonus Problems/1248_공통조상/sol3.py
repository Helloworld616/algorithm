# 교수님 해설

# class Node, Tree
# Tree => Node들의 합으로 구성
# Node : pk, parent, child1, child2
# Tree : Node * n

import sys
sys.stdin = open('input.txt')


class Node:
    def __init__(self, pk, parent=None, child=None):
        self.pk = pk
        self.parent = parent
        self.child1 = child
        self.child2 = None

    def add_child(self, pk):
        # 1번 자식이 있으면
        if self.child1:
            self.child2 = pk
        else:
            self.child1 = pk

    def add_parent(self, pk):
        self.parent = pk


class Tree:
    def __init__(self, info: str):
        data_list = list(map(int, info.split()))
        self.nodes = {}
        self.subtree_cnt = 0

        for i in range(len(data_list) // 2):
            parent_pk, child_pk = data_list[i*2:(i+1)*2]
            parent = self.nodes.get(parent_pk)
            child = self.nodes.get(child_pk)

            # 지금 들어온 parernt pk가 이미 트리에 없다면,
            if not parent:
                self.nodes[parent_pk] = Node(pk=parent, child=child_pk)
            else:
                parent.add_child(child_pk)

            if not child:
                self.nodes[child_pk] = Node(pk=child_pk, parent=parent_pk)
            else:
                child.add_parent(parent_pk)

    def get_ancestors(self, pk):
        ancestors = []
        node = self.nodes.get(pk)
        while node.parent:
            parent_pk = node.parent
            ancestors.append(parent_pk)
            node = self.nodes.get(parent_pk)
        return ancestors


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    tree = Tree(input())
    a1 = tree.get_ancestors(n1)
    a2 = tree.get_ancestors(n2)

    idx = -1
    while -idx <= len(a1) and a1[idx] == a2[idx]:
        idx -= 1
    idx += 1

    sub_root = a1[idx]

    # tree.count_subtree(sub_root)
    # print('#{} {}'.format(tc, ))
