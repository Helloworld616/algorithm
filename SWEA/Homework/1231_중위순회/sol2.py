import sys
sys.stdin = open('input.txt')


def inorder(node_no):
    if tree[node_no][2]:
        inorder(tree[node_no][0])
        ans.append(tree[node_no][2])
        inorder(tree[node_no][1])



T = 10
for tc in range(1, T+1):
    V = int(input())

    tree = [[0 for _ in range(3)] for _ in range(V+1)]

    for _ in range(V):
        # [node_no, node_data, left_child, right_child]
        input_data = input().split()
        node_no = int(input_data[0])
        node_data = input_data[1]

        # tree에 data 입력
        tree[node_no][2] = node_data

        # node_no * 2가 마지막 노드 번호(V)보다 작다 == 왼쪽 자식이 있다.
        if node_no * 2 <= V:
            tree[node_no][0] = int(input_data[2])
            # # node_no * 2 + 1이 마지막 노드 번호(V)보다 작다 == 오른쪽 자식이 있다.
            if node_no * 2 + 1 <= V:
                tree[node_no][1] = int(input_data[3])

        ans = []
        inorder(1)
        print('#{} {}'.format(tc, ''.join(ans)))