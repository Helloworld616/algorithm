# 시간초과

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def check_root():
    for key, value in enter_tree.items():
        if len(value) == 0:
            return key, True

    return 0, False


def check_edge(root):
    for key, value in enter_tree.items():
        if key == root:
            continue
        if len(value) != 1:
            return False

    return True


def check_traversal(root):
    result = []
    traversal(root, result)
    if len(result) == len(foray_tree) and len(set(result)) == len(set(foray_tree.keys())):
        return True

    return False


def traversal(node, result):
    result.append(node)
    if len(foray_tree[node]) != 0:
        for next_node in foray_tree[node]:
            traversal(next_node, result)


# main
k = 1
while True:
    nodes = []
    is_end = False

    while True:
        numbers = list(map(int, input().split()))
        nodes += numbers
        if nodes[-1] == 0 and nodes[-2] == 0:
            check = list(map(int, input().split()))
            if len(check) != 0:
                is_end = True
            break

    foray_tree = dict()
    enter_tree = dict()
    for i in range(0, len(nodes)-3, 2):
        if nodes[i] not in foray_tree:
            foray_tree[nodes[i]] = [nodes[i + 1]]
            enter_tree[nodes[i]] = []
        else:
            foray_tree[nodes[i]].append(nodes[i + 1])
        if nodes[i + 1] not in enter_tree:
            enter_tree[nodes[i + 1]] = [nodes[i]]
            foray_tree[nodes[i + 1]] = []
        else:
            enter_tree[nodes[i + 1]].append(nodes[i])

    if len(foray_tree) == 0:
        print(f'Case {k} is a tree.')
    else:
        root, is_root = check_root()
        if is_root:
            is_edge = check_edge(root)
            is_traversal = check_traversal(root)
            if is_edge and is_traversal:
                print(f'Case {k} is a tree.')
            else:
                print(f'Case {k} is not a tree.')
        else:
            print(f'Case {k} is not a tree.')

    k += 1

    if is_end:
        break





