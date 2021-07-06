import sys
sys.stdin = open('sample_input.txt')
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0

    while cnt < M:
        queue.append(queue.popleft())
        cnt += 1

    print('#{} {}'.format(tc, queue[0]))