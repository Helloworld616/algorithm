# 시간초과

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def is_tree():
    is_root = False
    for i in range(1, len(tree)):
        if not is_root and node_check[i] and len(tree[i]) == 0:
            is_root = True
        if is_root and node_check[i] and len(tree[i]) == 0:
            return False
        if node_check[i] and len(tree[i]) > 1:
            return False

    if not is_root:
        return False

    return True


# main
k = 1
while True:
    nodes = []
    is_end = False

    while True:
        numbers = list(map(int, input().split()))
        nodes += numbers
        if len(nodes) != 0 and nodes[-1] == 0 and nodes[-2] == 0:
            check = list(map(int, input().split()))
            if len(check) != 0:
                is_end = True
            break

    tree = [[] for _ in range(max(nodes) + 1)]
    node_check = [False for _ in range(max(nodes) + 1)]
    for i in range(0, len(nodes)-1, 2):
        tree[nodes[i+1]].append(nodes[i])
        node_check[nodes[i]] = True
        node_check[nodes[i+1]] = True

    if len(nodes) == 0:
        print(f'Case {k} is not a tree.')
    else:
        if len(tree) == 1:
            print(f'Case {k} is a tree.')
        else:
            flag = is_tree()
            if flag:
                print(f'Case {k} is a tree.')
            else:
                print(f'Case {k} is not a tree.')

    k += 1

    if is_end:
        sys.exit(0)
