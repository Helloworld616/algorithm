import sys
from collections import deque
sys.stdin = open('sample_input.txt')

'''
이 문제는 낚시 문제다 -_-;;;
문제 제목과 설명에서 이진 탐색 트리와 관련된 것처럼 위장하고 있지만 사실 아무런 관련 없다.

이 문제는 그저 단순한 '중위 순회' 문제일 뿐이다.
이진 탐색 트리라는 말에 현혹되어서 이진 탐색 트리의 삭제/삽입 방법만을 고민한다면 문제를 제대로 풀 수 없다.

'''


# 중위순회 함수
def inorder(tree, idx, num):
    # 인덱스가 N보다 작거나 같은 때에만 수행
    if idx <= N:
        # 왼쪽 자식 순회
        inorder(tree, idx*2, num)
        # 큐 num의 맨 앞 원소를 빼서 tree에 넣는다.
        tree[idx] = num.popleft()
        # 오른쪽 자식 순회
        inorder(tree, (idx*2)+1, num)


# main
T = int(input())
for tc in range(1, T+1):
    # 노드 갯수 입력 받기
    N = int(input())
    # 트리 생성 후 초기화
    tree = [0] * (N+1)

    # 큐 num 생성
    num = deque()
    # num에 1부터 N까지의 수를 차례대로 담는다.
    for i in range(1, N+1):
        num.append(i)

    # 중위순회 시행
    inorder(tree, 1, num)

    # 결과 출력
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
