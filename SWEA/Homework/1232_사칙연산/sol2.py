# 교수님 해설
import sys
sys.stdin = open('input.txt')

def inorder(node):
    data = tree[node][0]
    if data: # node_no == 0? => 이전 node가 leaf node냐?
        left, right = tree[node][1], tree[node][2]
        if data == '+':
            return inorder(left) + inorder(right)
        elif data == '-':
            return inorder(left) - inorder(right)
        elif data == '/':
            return inorder(left) / inorder(right)
        elif data == '*':
            return inorder(left) * inorder(right)
        # data가 숫자라면
        else:
            return data


T = 10
for tc in range(1, T+1):
    N = int(input())
    """
    tree = [
        ex: [data, left, right]
        0: [0, 0, 0]
        1: ['*', 2, 3]
        2: ['/', 4, 5]
        3: [3, 0, 0]
        4: [9, 0, 0]
        5: ['-', 6, 7]
        6: [6, 0, 0]
        7: [4, 0, 0]
    ]
    
    """
    tree = [[0 for _ in range(3)] for _ in range(N+1)]

    for _ in range(N):
        # [node_no, data (, left, right)]
        input_data = list(input().split())
        node_no = int(input_data[0])
        # data가 연산자라면,
        if len(input_data) > 2:
            # tree에 data 입력
            tree[node_no][0] = input_data[1]
            # tree에 left/right 입력
            tree[node_no][1] = int(input_data[2])
            tree[node_no][2] = int(input_data[3])
        # data가 숫자라면
        else:
            tree[node_no][0] = int(input_data[1])

    print(f'#{tc} {int(inorder(1))}')