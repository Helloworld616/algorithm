# 교수님 해설
import sys
sys.stdin = open('sample_input.txt')

def preorder(node):
    # 함수 진입 == node에 방문
    global cnt
    cnt += 1
    childs = tree[node] # [6]
    for new_node in childs:
        preorder(new_node)


T = int(input())

for tc in range(1, T+1):
    E, root_node = map(int, input().split())
    info = list(map(int, input().split()))

    # node의 개수 => E + 1
    # 0을 제외하므로 E + 2
    tree = [[] for _ in range(E+2)]

    """
    [
    0 []
    1 [6]
    2 [1, 5]
    3 []
    4 []
    5 [3]
    6 [4]
    ]
    """

    for i in range(E):
        parent, child = info[i*2:(i+1)*2]
        tree[parent].append(child)

    cnt = 0
    preorder(root_node)
    print(f'#{tc} {cnt}')
